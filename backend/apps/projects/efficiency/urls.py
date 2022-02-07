# -*- coding: utf-8 -*-
"""
Create by sandy at 16:34 09/12/2021
Description: ToDo
"""
from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.projects.efficiency.views import EfficiencyModelViewSet, ModuleModelViewSet

router = DefaultRouter()
router.register(r'efficiency', EfficiencyModelViewSet)
router.register(r'module', ModuleModelViewSet)

urlpatterns = [
    re_path('module/tree/', ModuleModelViewSet.as_view({'get': 'tree_select_list'})),
    re_path('module/children/', ModuleModelViewSet.as_view({'get': 'get_all'})),
]

urlpatterns += router.urls

