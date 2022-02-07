# Generated by Django 2.2.16 on 2021-12-22 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point', '0002_auto_20211210_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='name',
        ),
        migrations.AddField(
            model_name='point',
            name='en_name',
            field=models.CharField(default='', max_length=100, verbose_name='英文名称'),
        ),
        migrations.AddField(
            model_name='point',
            name='zh_name',
            field=models.CharField(default='', max_length=100, verbose_name='中文名称'),
        ),
    ]