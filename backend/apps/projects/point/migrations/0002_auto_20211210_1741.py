# Generated by Django 2.2.16 on 2021-12-10 17:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('point', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tool',
            new_name='Point',
        ),
    ]
