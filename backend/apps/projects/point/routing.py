# -*- coding: utf-8 -*-
"""
Create by sandy at 12:06 16/02/2022
Description: ToDo
"""
from django.urls import path

from apps.projects.point.consumers import PointCatchConsumer

websocket_urlpatterns = [
    path('point/catch/u<str:uid>/p<str:port>/', PointCatchConsumer.as_asgi()),
]

