
from django.contrib.auth import get_user_model
from apps.basics.op_drf.serializers import CustomModelSerializer
from apps.projects.point.models import Point, Suite

UserProfile = get_user_model()


class PointSerializer(CustomModelSerializer):
    """
    简单菜单序列化器
    """
    class Meta:
        model = Point
        # fields = '__all__'
        exclude = ('description', 'creator', 'modifier')


class SuiteSerializer(CustomModelSerializer):
    """
    简单菜单序列化器
    """
    class Meta:
        model = Suite
        # fields = '__all__'
        exclude = ('description', 'creator', 'modifier')
