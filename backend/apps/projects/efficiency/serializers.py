
from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.basics.op_drf.serializers import CustomModelSerializer
from apps.projects.efficiency.models import Efficiency
from apps.projects.efficiency.models import Module

UserProfile = get_user_model()


class EfficiencySerializer(CustomModelSerializer):
    """
    简单菜单序列化器
    """
    class Meta:
        model = Efficiency
        # fields = '__all__'
        exclude = ('description', 'creator', 'modifier')


class ModuleSerializer(CustomModelSerializer):
    """
    模块管理 简单序列化器
    """
    parentId = serializers.IntegerField(source="parentId.id", default=0)

    class Meta:
        model = Module
        exclude = ('description', 'creator', 'modifier')


class ModuleCreateUpdateSerializer(CustomModelSerializer):
    """
    模块管理 创建/更新时的列化器
    """

    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = Module
        fields = '__all__'


class ModuleTreeSerializer(serializers.ModelSerializer):
    """
    模块树形架构序列化器:递归序列化所有深度的子模块
    """
    label = serializers.CharField(source='name', default='')
    parentId = serializers.IntegerField(source="parentId.id", default=0)

    class Meta:
        model = Module
        fields = ('id', 'label', 'parentId', 'status')
