# -*- coding: utf-8 -*-
"""
Create by sandy at 12:05 16/02/2022
Description: ToDo
"""

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from apps.projects.point import routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
