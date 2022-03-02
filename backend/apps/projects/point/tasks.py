# -*- coding: utf-8 -*-
"""
Create by sandy at 11:35 21/02/2022
Description: ToDo
"""

from __future__ import absolute_import

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from application.celery import app
import logging
import os

from application.settings import BASE_DIR

logger = logging.getLogger('log')


@app.task
def send_msg_task(message, group=None):
    async_to_sync(get_channel_layer().group_send)(
        group, {
            "type": "send.message",
            "message": message
        }
    )


@app.task
def start_mitmproxy(port, uid):
    path = os.path.join(BASE_DIR, 'manage.py')
    os.system(f'python3 {path} mitmproxyCommand {port} {uid} --start')


@app.task
def close_mitmproxy(port):
    result = os.popen(f"lsof -i:{port} | grep LISTEN").read()
    if result:
        pid = [ele for ele in result.split(' ') if ele][1]
        os.popen(f'kill -9 {pid}')



