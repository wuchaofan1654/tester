
from django.contrib.auth import get_user_model
from apps.basics.op_drf.serializers import CustomModelSerializer
from apps.basics.permission.serializers import DeptSerializer
from apps.projects.api.models import Api
from apps.projects.api.models import Suite
from apps.projects.api.models import RpcItem
from apps.projects.api.models import RpcRecord

UserProfile = get_user_model()


class ApiSerializer(CustomModelSerializer):
    """
    简单菜单序列化器
    """
    class Meta:
        model = Api
        # fields = '__all__'
        exclude = ('description', 'creator', 'modifier')


class SuiteSerializer(CustomModelSerializer):
    """
    简单菜单序列化器
    """
    dept = DeptSerializer(read_only=True)

    class Meta:
        model = Suite
        # fields = '__all__'
        exclude = ('description', 'creator', 'modifier')


class RpcItemSerializer(CustomModelSerializer):
    """
    简单菜单序列化器
    """
    class Meta:
        model = RpcItem
        # fields = '__all__'
        exclude = ('description', 'creator', 'modifier')


class RpcRecordSerializer(CustomModelSerializer):
    """
    简单菜单序列化器
    """
    items = RpcItemSerializer(many=True)

    class Meta:
        model = RpcRecord
        # fields = ['items']
        exclude = ('description', 'creator', 'modifier')
