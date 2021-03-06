# Generated by Django 2.2.16 on 2022-01-04 16:38

import apps.basics.op_drf.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RpcRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.basics.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', apps.basics.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', apps.basics.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.basics.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('item_ids', models.CharField(default=str, max_length=100, verbose_name='rpc方法列表')),
                ('result', models.IntegerField(choices=[(0, '未执行'), (1, '成功'), (2, '失败'), (3, '阻塞'), (4, '部分失败')], default=1, verbose_name='执行状态')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name_plural': 'RPC记录',
            },
        ),
        migrations.CreateModel(
            name='RpcItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.basics.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', apps.basics.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', apps.basics.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.basics.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('item_name', models.CharField(default=str, max_length=100, verbose_name='名称')),
                ('status', models.IntegerField(choices=[(0, '禁用'), (1, '正常'), (2, '仅自己可见')], default=1, verbose_name='状态')),
                ('is_leaf', models.IntegerField(choices=[(0, '否'), (1, '是')], default=0, verbose_name='是否根结点')),
                ('params', models.TextField(default=str, verbose_name='请求参数')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.RpcItem')),
            ],
            options={
                'verbose_name_plural': 'RPC方法',
            },
        ),
    ]
