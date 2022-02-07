from django.shortcuts import render

# Create your views here.
from rest_framework.request import Request

from apps.basics.op_drf.filters import DataLevelPermissionsFilter
from apps.basics.op_drf.response import SuccessResponse
from apps.basics.op_drf.viewsets import CustomModelViewSet
from apps.basics.permission.permissions import CommonPermission
from apps.projects.efficiency.filters import EfficiencyFilter
from apps.projects.efficiency.models import Efficiency, Module
from apps.projects.efficiency.serializers import EfficiencySerializer, ModuleSerializer, ModuleCreateUpdateSerializer, \
    ModuleTreeSerializer


class EfficiencyModelViewSet(CustomModelViewSet):
    """
    小工具管理 的CRUD视图
    """
    queryset = Efficiency.objects.all()
    serializer_class = EfficiencySerializer
    filter_class = EfficiencyFilter
    # 权限控制
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    search_fields = ('name',)
    ordering = ['create_datetime']  # 默认排序

    module_set = set()

    def list(self, request: Request, *args, **kwargs):
        self.module_set = set()
        module_query_sets = Module.objects.all()
        parent_id = request.GET.get('parentId')
        if parent_id:
            self.get_module_ids_by_parent_id(parent_id, module_query_sets)
            efficiency_query_sets = Efficiency.objects.filter(module_id__in=list(self.module_set))

        else:
            efficiency_query_sets = Efficiency.objects.filter()

        data = {
            "count": len(efficiency_query_sets),
            "results": []
        }
        page_size = int(request.GET.get('pageSize', 20))
        page_num = int(request.GET.get('pageNum', 1))
        efficiency_query_sets = efficiency_query_sets[(page_num - 1) * page_size: page_num * page_size]

        serializer = EfficiencySerializer(efficiency_query_sets, many=True)
        data["results"] = serializer.data
        return SuccessResponse(data)

    def get_module_ids_by_parent_id(self, parent_id, data=None, include_parent_id=True):
        if include_parent_id:
            self.module_set.add(parent_id)

        if not data:
            data = []

        data = [d for d in data if d.parentId]
        children = [d for d in data if str(d.parentId.id) == parent_id]

        if children:
            [self.module_set.add(child.id) for child in children]
            [self.get_module_ids_by_parent_id(child.id, data) for child in children]


class ModuleModelViewSet(CustomModelViewSet):
    """
    模块管理 的CRUD视图
    """
    queryset = Module.objects.all()
    serializer_class = ModuleTreeSerializer
    create_serializer_class = ModuleCreateUpdateSerializer
    update_serializer_class = ModuleCreateUpdateSerializer
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    search_fields = ('name',)
    ordering = 'create_datetime'  # 默认排序

    children_ids_set = set()

    def tree_select_list(self, request: Request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if hasattr(self, 'handle_logging'):
            self.handle_logging(request, *args, **kwargs)
        serializer = ModuleTreeSerializer(queryset, many=True)
        return SuccessResponse(serializer.data)
