# -*- coding: utf-8 -*-
"""
Create by sandy at 14:37 21/02/2022
Description: ToDo
"""


import os


def kill_progress_by_port(port):
    result = os.popen(f"lsof -i:{port} | grep LISTEN").read()
    if result:
        pid = [ele for ele in result.split(' ') if ele][1]
        os.popen(f'kill -9 {pid}')


kill_progress_by_port(9998)
