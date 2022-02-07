from django.shortcuts import render

# Create your views here.

from apps.basics.op_drf.filters import DataLevelPermissionsFilter
from apps.basics.op_drf.viewsets import CustomModelViewSet
from apps.basics.permission.permissions import CommonPermission
from apps.projects.case.models import Case
from apps.projects.case.models import Suite
from apps.projects.case.models import Record
from apps.projects.case.serializers import CaseSerializer
from apps.projects.case.serializers import SuiteSerializer
from apps.projects.case.serializers import RecordSerializer


class CaseModelViewSet(CustomModelViewSet):
    """
    用例管理 的CRUD视图
    """
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    # 权限控制
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    search_fields = ('name',)
    ordering = ['create_datetime']  # 默认排序


class SuiteModelViewSet(CustomModelViewSet):
    """
    用例集管理 的CRUD视图
    """
    queryset = Suite.objects.all()
    serializer_class = SuiteSerializer
    # 权限控制
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    search_fields = ('name',)
    ordering = ['create_datetime']  # 默认排序


class RecordModelViewSet(CustomModelViewSet):
    """
    用例执行记录管理 的CRUD视图
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    # 权限控制
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    ordering = ['create_datetime']  # 默认排序
