from django.shortcuts import render

# Create your views here.
from apps.basics.op_drf.filters import DataLevelPermissionsFilter
from apps.basics.op_drf.viewsets import CustomModelViewSet
from apps.basics.permission.permissions import CommonPermission
from apps.projects.point.filters import PointFilter
from apps.projects.point.models import Point
from apps.projects.point.models import Suite
from apps.projects.point.serializers import PointSerializer
from apps.projects.point.serializers import SuiteSerializer


class PointModelViewSet(CustomModelViewSet):
    """
    埋点管理 的CRUD视图
    """
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    filter_class = PointFilter
    # 权限控制
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    search_fields = ('name',)
    ordering = ['key_yn', 'create_datetime']  # 默认排序


class SuiteModelViewSet(CustomModelViewSet):
    """
    埋点集管理 的CRUD视图
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
