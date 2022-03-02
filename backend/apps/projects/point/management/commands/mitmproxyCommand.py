# -*- coding: utf-8 -*-
"""
Create by sandy at 14:25 23/12/2021
Description: ToDo
"""
from django.core.management import BaseCommand

from apps.projects.point.management.commands.mitmproxyUtil import MitmproxyUtil
from apps.projects.point.signals import mitmproxy_started_signal_callback


class Command(BaseCommand):
    """
    mitmproxy脚本
    @action: start, quit
    @evn: pro, test
    """

    def add_arguments(self, parser):
        parser.add_argument('port', nargs='?', type=int)
        parser.add_argument('uid', nargs='?', type=int)
        parser.add_argument('--start',
                            action='store_true',
                            dest='start',
                            default=False,
                            help='do start command')
        parser.add_argument('--stop',
                            action='store_true',
                            dest='stop',
                            default=False,
                            help='do stop command')

    def handle(self, *args, **kwargs):
        try:
            print("===================started")
            mitmproxy_started_signal_callback.send(self, action='start')
            mit = MitmproxyUtil(
                group=f"u{kwargs.get('uid')}_p{kwargs.get('port')}",
                listen_port=kwargs.get('port'),
                allow_hosts=[]
            )

            kwargs.get('start') and mit.start()
            kwargs.get('stop') and mit.quit()

        except Exception as err:
            return err
