# -*- coding: utf-8 -*-
"""
Create by sandy at 11:00 23/12/2021
Description: ToDo
"""

from django.dispatch import receiver
from django.db.models.signals import post_save, post_init
from apps.projects.point.models import Point
from django.dispatch import Signal


@receiver(signal=post_init, sender=Point, dispatch_uid='point_pre_init_signal_11')
def point_init_callback(sender, instance=None, created=False, **kwargs):
    print(f"==========={sender}============")
    point_received_signal.send(sender=sender)


@receiver(signal=post_save, sender=Point, dispatch_uid='point_saved_signal')
def point_save_callback(sender, instance=None, created=False, **kwargs):
    if created:
        point_received_signal.send(sender=sender, msg='my signal called by point init callback')


# self defined signals
# mitmproxy 接收到埋点信息
point_received_signal = Signal()


@receiver(point_received_signal)
def point_received_signal_callback_check(sender, **kwargs):
    """
    @sender: 埋点信息
    检查埋点是否正确
    """
    print(f'point_received_signal_callback_check: {sender}')


@receiver(point_received_signal)
def point_received_signal_callback_save(sender, **kwargs):
    """
    埋点信息入库
    """
    print(f'point_received_signal_callback_save: {sender}')



