# Create your models here.
from django.db.models import CharField, IntegerField, ForeignKey, CASCADE, TextField

from apps.basics.op_drf.models import CoreModel
from apps.projects.utils.modelChoices import STATUS_CHOICES


class Module(CoreModel):
    name = CharField(max_length=64, verbose_name="模块名称")
    orderNum = IntegerField(verbose_name="显示排序")
    status = CharField(max_length=8, verbose_name="状态", null=True, blank=True)
    parentId = ForeignKey(to='Module', on_delete=CASCADE, default=False, verbose_name="上级模块",
                          db_constraint=False, null=True, blank=True)

    class Meta:
        verbose_name = '模块管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.name}'


class Efficiency(CoreModel):
    name = CharField(verbose_name='名称', max_length=100, default=str, db_index=True)
    module = ForeignKey(verbose_name='模块', to='Module', default=False, on_delete=CASCADE)
    command = TextField(verbose_name="脚本命令", default='# encoding=utf-8\n')
    status = IntegerField(verbose_name='状态', default=1, choices=STATUS_CHOICES)

    class Meta:
        verbose_name_plural = "小工具"

    def __str__(self):
        return self.name
