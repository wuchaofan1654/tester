# -*- coding: utf-8 -*-
"""
Create by sandy at 14:25 23/12/2021
Description: ToDo
"""
from django.core.management import BaseCommand

import mitmproxy.http
from mitmproxy import options, proxy
from mitmproxy.tools.dump import DumpMaster
import base64
import gzip
import io
import json
import urllib.parse

# from backend.points.tasks import send_point_to_ws


class PointAnalysis(object):
    def __init__(self, group):
        self.group = group

    def request(self, flow: mitmproxy.http.HTTPFlow) -> None:
        request_data = flow.request
        request_form = request_data.urlencoded_form
        points = self.decrypt_request_form(request_form)
        # send_point_to_ws.delay(self.group, points)

    @staticmethod
    def decrypt_request_form(request_form):
        if request_form.get('gzip') != '1':
            return {'data': []}

        _cont = urllib.parse.unquote(request_form['data_list'])
        gzip_buff = base64.b64decode(_cont)
        buff = io.BytesIO(gzip_buff)

        with gzip.GzipFile(fileobj=buff) as f:
            data_str = f.read().decode('utf-8')

        json_data = json.loads(data_str)
        return [item['properties']['event_params'] for item in json_data if item['event'] in 'app_event']


class MitmproxyUtil(object):
    def __init__(self, group, listen_port=9999, allow_hosts=None):
        self.addon = PointAnalysis(group=group)
        self.opts = options.Options(
            listen_port=listen_port,
            allow_hosts=allow_hosts or ['http://testst3.soyoung.com/md/shence'],
        )
        self.p_conf = proxy.config.ProxyConfig(self.opts)
        self.m = DumpMaster(self.opts)
        self.m.server = proxy.server.ProxyServer(self.p_conf)
        self.m.addons.add(self.addon)

    def quit(self):
        if not self.m.running():
            return
        self.m.shutdown()

    def start(self):
        try:
            self.m.run()
        except KeyboardInterrupt:
            self.m.shutdown()


class Command(BaseCommand):
    """
    mitmproxy脚本
    @action: start, quit
    @evn: pro, test
    """
    def add_arguments(self, parser):
        parser.add_argument('action', nargs='*', type=str, )
        parser.add_argument('evn', nargs='*', type=str, )

    def handle(self, *args, **kwargs):
        if kwargs['evn'] == 'test':
            pass

