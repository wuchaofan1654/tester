from django.db import models

from apps.basics.op_drf.models import CoreModel
from apps.basics.permission.models import Dept
from apps.projects.utils.modelChoices import EXECUTE_STATUS_CHOICES, STATUS_CHOICES


class Api(CoreModel):
    name = models.CharField(verbose_name='接口名称', max_length=100, default=str)
    url = models.CharField(verbose_name='请求url', max_length=200, default=str)
    headers = models.TextField(verbose_name='请求头信息', null=True, blank=True, default=dict)
    params = models.TextField(verbose_name='请求参数', null=True, blank=True, default=dict)
    validators = models.TextField(verbose_name='验证器', null=True, blank=True, default=list)
    extractors = models.TextField(verbose_name='提取器', null=True, blank=True, default=list)
    desc = models.CharField(verbose_name='接口描述', max_length=200, default=str, null=True, blank=True)
    last_exe_status = models.IntegerField(verbose_name='最后执行状态', choices=EXECUTE_STATUS_CHOICES, default=0)
    status = models.IntegerField(verbose_name='状态', default=1, choices=STATUS_CHOICES)

    class Meta:
        verbose_name_plural = "接口"

    def __str__(self):
        return self.name


class Suite(CoreModel):
    dept = models.ForeignKey(verbose_name='模块分类', default=1, to=Dept, related_name='api_suite_dept',
                             on_delete=models.CASCADE)
    apis = models.ManyToManyField(verbose_name='接口', to=Api)
    name = models.CharField(verbose_name='用例集名称', max_length=100, default=str)
    status = models.IntegerField(verbose_name='状态', default=1, choices=STATUS_CHOICES)

    class Meta:
        verbose_name_plural = "接口集"

    def __str__(self):
        return self.name


class RpcItem(CoreModel):
    LEAF_CHOICES = ((False, '否'), (True, '是'))
    item_name = models.CharField(verbose_name='名称', max_length=100, default=str)
    level = models.IntegerField(verbose_name='层级', default=0)
    parent = models.ForeignKey(to='RpcItem', on_delete=models.CASCADE, default=0, blank=True, null=True)
    status = models.IntegerField(verbose_name='状态', default=1, choices=STATUS_CHOICES)
    is_leaf = models.BooleanField(verbose_name='是否末结点', default=False, choices=LEAF_CHOICES)
    params = models.TextField(verbose_name='请求参数', default=str, blank=True, null=True)

    class Meta:
        verbose_name_plural = "RPC方法"
        ordering = ['level', '-id']

    def __str__(self):
        return self.item_name


class RpcRecord(CoreModel):
    items = models.ManyToManyField(verbose_name='rpc方法', to='RpcItem', default=0)
    result = models.IntegerField(verbose_name='执行状态', default=0, choices=EXECUTE_STATUS_CHOICES)

    class Meta:
        verbose_name_plural = "RPC记录"
        ordering = ['-id']

