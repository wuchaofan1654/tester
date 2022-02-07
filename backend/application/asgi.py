import os

import django

from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')
django.setup()

websocket_urlpatterns = [
]

application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    # Just HTTP for now. (We can add other protocols later.)
    'websocket': AuthMiddlewareStack(URLRouter(websocket_urlpatterns, )),
})
