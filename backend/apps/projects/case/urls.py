# -*- coding: utf-8 -*-
"""
Create by sandy at 16:34 09/12/2021
Description: ToDo
"""
from rest_framework.routers import DefaultRouter

from apps.projects.case.views import CaseModelViewSet
from apps.projects.case.views import SuiteModelViewSet
from apps.projects.case.views import RecordModelViewSet

router = DefaultRouter()
router.register(r'case', CaseModelViewSet)
router.register(r'suite', SuiteModelViewSet)
router.register(r'record', RecordModelViewSet)

urlpatterns = [
]

urlpatterns += router.urls

