# Generated by Django 2.2.16 on 2022-01-07 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20220107_1657'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rpcitem',
            options={'ordering': ['-id'], 'verbose_name_plural': 'RPC方法'},
        ),
        migrations.AlterModelOptions(
            name='rpcrecord',
            options={'ordering': ['-id'], 'verbose_name_plural': 'RPC记录'},
        ),
        migrations.RemoveField(
            model_name='rpcrecord',
            name='items',
        ),
        migrations.AddField(
            model_name='rpcrecord',
            name='items',
            field=models.CharField(default=str, max_length=255, verbose_name='rpc方法'),
        ),
    ]
