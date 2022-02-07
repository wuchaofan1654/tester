# -*- coding: utf-8 -*-
"""
Create by sandy at 16:34 09/12/2021
Description: ToDo
"""
from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.basics.system.views import SystemInfoApiView
from apps.projects.point.views import PointModelViewSet
from apps.projects.point.views import SuiteModelViewSet

router = DefaultRouter()
router.register(r'point', PointModelViewSet)
router.register(r'suite', SuiteModelViewSet)

urlpatterns = [
    re_path('catch/', SystemInfoApiView.as_view()),
]

urlpatterns += router.urls

