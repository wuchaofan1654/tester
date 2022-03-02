# -*- coding: utf-8 -*-
"""
Create by sandy at 14:25 22/02/2022
Description: ToDo
"""

from apps.projects.point.tasks import send_msg_task
from mitmproxy import options, proxy
from mitmproxy.tools.dump import DumpMaster
import mitmproxy.http
import base64
import gzip
import io
import json
import urllib.parse


class PointAnalysis(object):
    def __init__(self, group):
        self.group = group

    def request(self, flow: mitmproxy.http.HTTPFlow) -> None:
        request_data = flow.request
        if 'st3.soyoung' in request_data.url:
            request_form = request_data.urlencoded_form
            points = self.decrypt_request_form(request_form)
            [send_msg_task.delay(point, f'{self.group}') for point in points]
        elif 'sydata' in request_data.url:
            request_form = request_data.urlencoded_form
            points = self.decrypt_request_form(request_form)
            [send_msg_task.delay(point, f'{self.group}') for point in points]

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
            allow_hosts=allow_hosts,
            ssl_version_client="all",
            ssl_version_server="all",
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

