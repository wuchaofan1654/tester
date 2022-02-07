import json

# Create your views here.
import requests
from rest_framework.request import Request

from apps.basics.op_drf.filters import DataLevelPermissionsFilter
from apps.basics.op_drf.response import SuccessResponse, ErrorResponse
from apps.basics.op_drf.viewsets import CustomModelViewSet
from apps.basics.permission.permissions import CommonPermission
from apps.projects.api.filters import RpcRecordFilter
from apps.projects.api.models import Api
from apps.projects.api.models import Suite
from apps.projects.api.models import RpcItem
from apps.projects.api.models import RpcRecord
from apps.projects.api.serializers import ApiSerializer
from apps.projects.api.serializers import SuiteSerializer
from apps.projects.api.serializers import RpcItemSerializer
from apps.projects.api.serializers import RpcRecordSerializer


class ApiModelViewSet(CustomModelViewSet):
    """
    接口管理 的CRUD视图
    """
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
    # 权限控制
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    search_fields = ('name',)
    ordering = ['create_datetime']  # 默认排序


class SuiteModelViewSet(CustomModelViewSet):
    """
    接口集管理 的CRUD视图
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


class RpcItemModelViewSet(CustomModelViewSet):
    """
    接口集管理 的CRUD视图
    """
    queryset = RpcItem.objects.all()
    serializer_class = SuiteSerializer
    # 权限控制
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    search_fields = ('item_name',)
    ordering = ['create_datetime']  # 默认排序

    def get_rpc_items(self, request, parent_id=None):
        queryset = self.get_queryset()
        condition = parent_id and {"parent_id": parent_id} or {"parent_id__isnull": True}
        queryset = queryset.filter(**condition)
        serialized_data = RpcItemSerializer(queryset, many=True).data
        return SuccessResponse(serialized_data)

    @staticmethod
    def execute_rpc(request: Request, *args, **kwargs):
        try:
            data = request.data
            record = RpcRecord.objects.create(creator_id=request.user.id)
            item_ids = [item['id'] for item in data['items']]
            record.items.add(*tuple(item_ids))
            record.save()
            host = data.get('env')
            routes = ', '.join([f'\'{item["item_name"]}\'' for item in data.get('items')[:-1]])
            method = data.get('items')[-1]['item_name']
            params = data.get('params') and data.get('params') or data.get('items')[-1].get('params', {})
            params = json.loads(params)
            params = ', '.join([f'{k}=\'{v}\'' for k, v in params.items()])
            url = f"{host}/testRpc/rpc?rpc=RPC({routes})->{method}({params})"
            data = requests.get(url)
            return SuccessResponse(data.json())

        except Exception as err:
            return ErrorResponse(str(err))


class RpcRecordModelViewSet(CustomModelViewSet):
    """
    Rpc执行记录管理 的CRUD视图
    """
    queryset = RpcRecord.objects.all()
    serializer_class = RpcRecordSerializer
    filter_class = RpcRecordFilter
    # 权限控制
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    ordering = ['-create_datetime']

    def get_rpc_records(self, request):
        queryset = self.get_queryset()
        queryset = queryset.filter(
            creator_id=request.user.id,
            creator=request.user.id
        )
        page = self.paginate_queryset(queryset)
        if page is not None:
            if getattr(self, 'values_queryset', None):
                return self.get_paginated_response(page)
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        if getattr(self, 'values_queryset', None):
            return SuccessResponse(page)
        serializer = self.get_serializer(queryset, many=True)
        return SuccessResponse(serializer.data)


