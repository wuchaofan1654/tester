# Generated by Django 2.2.16 on 2021-12-23 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='cases',
            field=models.ManyToManyField(to='case.Case', verbose_name='关联用例'),
        ),
    ]
