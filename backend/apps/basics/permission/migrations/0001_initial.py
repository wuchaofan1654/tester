# Generated by Django 2.2.16 on 2021-12-09 17:10

import apps.basics.op_drf.fields
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('description', apps.basics.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', apps.basics.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', apps.basics.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.basics.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('username', models.CharField(db_index=True, max_length=150, unique=True, verbose_name='用户账号')),
                ('secret', models.CharField(default=uuid.uuid4, max_length=255, verbose_name='加密秘钥')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='邮箱')),
                ('mobile', models.CharField(blank=True, max_length=255, null=True, verbose_name='电话')),
                ('avatar', models.TextField(blank=True, null=True, verbose_name='头像')),
                ('name', models.CharField(max_length=40, verbose_name='姓名')),
                ('gender', models.CharField(blank=True, max_length=8, null=True, verbose_name='性别')),
                ('remark', models.TextField(null=True, verbose_name='备注')),
                ('user_type', models.IntegerField(default=0, verbose_name='用户类型')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.basics.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', apps.basics.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', apps.basics.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.basics.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('deptName', models.CharField(max_length=64, verbose_name='部门名称')),
                ('orderNum', models.IntegerField(verbose_name='显示排序')),
                ('owner', models.CharField(blank=True, max_length=32, null=True, verbose_name='负责人')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='联系电话')),
                ('email', models.CharField(blank=True, max_length=32, null=True, verbose_name='邮箱')),
                ('status', models.CharField(blank=True, max_length=8, null=True, verbose_name='部门状态')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('parentId', models.ForeignKey(blank=True, db_constraint=False, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='permission.Dept', verbose_name='上级部门')),
            ],
            options={
                'verbose_name': '部门管理',
                'verbose_name_plural': '部门管理',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.basics.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', apps.basics.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', apps.basics.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.basics.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('menuType', models.CharField(max_length=8, verbose_name='菜单类型')),
                ('icon', models.CharField(blank=True, max_length=64, null=True, verbose_name='菜单图标')),
                ('name', models.CharField(max_length=64, verbose_name='菜单名称')),
                ('orderNum', models.IntegerField(verbose_name='显示排序')),
                ('isFrame', models.CharField(max_length=8, verbose_name='是否外链')),
                ('web_path', models.CharField(blank=True, max_length=128, null=True, verbose_name='前端路由地址')),
                ('component_path', models.CharField(blank=True, max_length=128, null=True, verbose_name='前端组件路径')),
                ('interface_path', models.CharField(blank=True, max_length=256, null=True, verbose_name='后端接口路径')),
                ('interface_method', models.CharField(default='GET', max_length=16, verbose_name='接口请求方式')),
                ('perms', models.CharField(blank=True, max_length=256, null=True, verbose_name='权限标识')),
                ('status', models.CharField(max_length=8, verbose_name='菜单状态')),
                ('visible', models.CharField(max_length=8, verbose_name='显示状态')),
                ('isCache', models.CharField(max_length=8, verbose_name='是否缓存')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('parentId', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='permission.Menu', verbose_name='上级菜单')),
            ],
            options={
                'verbose_name': '菜单管理',
                'verbose_name_plural': '菜单管理',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.basics.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', apps.basics.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', apps.basics.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.basics.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('roleName', models.CharField(max_length=64, verbose_name='角色名称')),
                ('roleKey', models.CharField(max_length=64, verbose_name='权限字符')),
                ('roleSort', models.IntegerField(verbose_name='角色顺序')),
                ('status', models.CharField(max_length=8, verbose_name='角色状态')),
                ('admin', models.BooleanField(default=False, verbose_name='是否为admin')),
                ('dataScope', models.CharField(choices=[('1', '全部数据权限'), ('2', '自定数据权限'), ('3', '本部门数据权限'), ('4', '本部门及以下数据权限'), ('5', '仅本人数据权限')], default='1', max_length=8, verbose_name='权限范围')),
                ('remark', models.TextField(blank=True, help_text='备注', null=True, verbose_name='备注')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
                ('dept', models.ManyToManyField(db_constraint=False, to='permission.Dept', verbose_name='数据权限-关联部门')),
                ('menu', models.ManyToManyField(db_constraint=False, to='permission.Menu', verbose_name='关联菜单权限')),
            ],
            options={
                'verbose_name': '角色管理',
                'verbose_name_plural': '角色管理',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', apps.basics.op_drf.fields.DescriptionField(blank=True, default='', help_text='描述', null=True, verbose_name='描述')),
                ('modifier', apps.basics.op_drf.fields.ModifierCharField(blank=True, help_text='该记录最后修改者', max_length=255, null=True, verbose_name='修改者')),
                ('dept_belong_id', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据归属部门')),
                ('update_datetime', apps.basics.op_drf.fields.UpdateDateTimeField(auto_now=True, help_text='修改时间', null=True, verbose_name='修改时间')),
                ('create_datetime', apps.basics.op_drf.fields.CreateDateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('postName', models.CharField(max_length=64, verbose_name='岗位名称')),
                ('postCode', models.CharField(max_length=32, verbose_name='岗位编码')),
                ('postSort', models.IntegerField(verbose_name='岗位顺序')),
                ('status', models.CharField(max_length=8, verbose_name='岗位状态')),
                ('remark', models.TextField(blank=True, help_text='备注', null=True, verbose_name='备注')),
                ('creator', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='创建者')),
            ],
            options={
                'verbose_name': '岗位管理',
                'verbose_name_plural': '岗位管理',
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='dept',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='permission.Dept', verbose_name='归属部门'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='post',
            field=models.ManyToManyField(db_constraint=False, to='permission.Post', verbose_name='关联岗位'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.ManyToManyField(db_constraint=False, to='permission.Role', verbose_name='关联角色'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
