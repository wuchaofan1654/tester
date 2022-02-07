from django.conf import settings
from django.db import models
from django.db.models import CharField, TextField, IntegerField, SET_NULL, CASCADE, ForeignKey

from apps.basics.op_drf.models import CoreModel
from apps.basics.permission.models import Dept
from apps.projects.utils.modelChoices import STATUS_CHOICES


class Point(CoreModel):
    zh_name = CharField(max_length=100, default='', verbose_name='中文名称')
    en_name = CharField(max_length=100, default='', verbose_name='英文名称')
    p_type = IntegerField(default=1, verbose_name='埋点类型')
    key_yn = IntegerField(default=0, verbose_name='标记核心')
    status = IntegerField(default=1, verbose_name='埋点状态')
    page_ext = TextField(verbose_name='页面扩展信息')
    action_ext = TextField(verbose_name='事件扩展信息')

    class Meta:
        verbose_name = '埋点'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.zh_name}"


class Suite(CoreModel):
    dept = models.ForeignKey(verbose_name='所属团队', to=Dept, default=0, related_name='point_suite_dept',
                             on_delete=models.CASCADE)
    name = CharField(verbose_name='用例集名称', max_length=100, default=str)
    points = models.ManyToManyField(verbose_name='埋点列表', to=Point)
    status = IntegerField(verbose_name='状态', default=1, choices=STATUS_CHOICES)
    creator = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_query_name='creator_query', null=True,
                                related_name='point_suite_creator', verbose_name='创建者', on_delete=SET_NULL,
                                db_constraint=False)  # 创建者

    class Meta:
        verbose_name_plural = "埋点集"

    def __str__(self):
        return self.name

