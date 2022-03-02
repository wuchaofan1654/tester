from channels.generic.websocket import AsyncWebsocketConsumer
from apps.projects.point.tasks import start_mitmproxy, close_mitmproxy
import json


class PointCatchConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uid = 1
        self.port = 9999
        self.group_name = None

    async def connect(self):
        self.uid = self.scope['url_route']['kwargs']['uid']
        self.port = self.scope['url_route']['kwargs']['port']
        self.group_name = f"u{self.uid}_p{self.port}"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
        start_mitmproxy.delay(self.port, self.uid)

    async def disconnect(self, close_code):
        close_mitmproxy(self.port)
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'send.message',
                'message': message
            }
        )

    async def send_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))
