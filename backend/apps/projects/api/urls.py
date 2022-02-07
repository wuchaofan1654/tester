# -*- coding: utf-8 -*-
"""
Create by sandy at 16:34 09/12/2021
Description: ToDo
"""
from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.projects.api.views import ApiModelViewSet
from apps.projects.api.views import SuiteModelViewSet
from apps.projects.api.views import RpcItemModelViewSet
from apps.projects.api.views import RpcRecordModelViewSet

router = DefaultRouter()
router.register(r'api', ApiModelViewSet)
router.register(r'suite', SuiteModelViewSet)
router.register(r'rpc/record', RpcRecordModelViewSet)

urlpatterns = [
    re_path('rpc/p(?P<parent_id>.*)/', RpcItemModelViewSet.as_view({'get': 'get_rpc_items'})),
    re_path('rpc/execute/', RpcItemModelViewSet.as_view({'post': 'execute_rpc'})),
    re_path('rpc/records/', RpcRecordModelViewSet.as_view({'get': 'get_rpc_records'})),

]

urlpatterns += router.urls

