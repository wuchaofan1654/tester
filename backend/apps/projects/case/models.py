from django.conf import settings
from django.db import models
from django.db.models import SET_NULL

from apps.basics.op_drf.models import CoreModel
from apps.basics.permission.models import Dept
from apps.projects.utils.modelChoices import STATUS_CHOICES, EXECUTE_STATUS_CHOICES


class Suite(CoreModel):
    dept = models.ForeignKey(verbose_name='所属团队', default=0, to=Dept, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='用例集名称', max_length=100, default=str)
    testcase_cnt = models.IntegerField(verbose_name='总用例数', default=0)
    success_cnt = models.IntegerField(verbose_name='成功用例数', default=0)
    failed_cnt = models.IntegerField(verbose_name='失败用例数', default=0)
    jared_cnt = models.IntegerField(verbose_name='阻塞用例数', default=0)
    status = models.IntegerField(verbose_name='状态', default=1, choices=STATUS_CHOICES)
    creator = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_query_name='creator_query', null=True,
                                related_name='case_suite_creator', verbose_name='创建者', on_delete=SET_NULL,
                                db_constraint=False)  # 创建者

    class Meta:
        verbose_name_plural = "用例集"
        ordering = ['-id']

    def __str__(self):
        return self.name


class Case(CoreModel):
    suite = models.ManyToManyField(verbose_name='用例集id', to=Suite)
    fid = models.IntegerField(verbose_name='父级ID', default=0)
    name = models.CharField(verbose_name="用例名称", default=str, max_length=255)
    level = models.IntegerField(verbose_name="优先级", default=3)
    related_users = models.ManyToManyField(verbose_name='执行人', to=settings.AUTH_USER_MODEL)
    status = models.IntegerField(verbose_name='状态', default=1, choices=STATUS_CHOICES)
    sort = models.IntegerField(verbose_name='排序字段', default=0)
    creator = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_query_name='creator_query', null=True,
                                related_name='case_creator', verbose_name='创建者', on_delete=SET_NULL,
                                db_constraint=False)  # 创建者

    class Meta:
        verbose_name_plural = "用例"
        ordering = ['id']
        index_together = ["id", "fid"]

    def __str__(self):
        return self.name


class Record(CoreModel):
    cases = models.ManyToManyField(verbose_name='关联用例', to=Case)
    status = models.IntegerField(verbose_name="执行状态", default=1, choices=EXECUTE_STATUS_CHOICES)
    creator = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_query_name='creator_query', null=True,
                                related_name='case_record_creator', verbose_name='创建者', on_delete=SET_NULL,
                                db_constraint=False)  # 创建者

    class Meta:
        verbose_name_plural = "记录"
        ordering = ['-id']
