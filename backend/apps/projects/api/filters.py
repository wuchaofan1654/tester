# -*- coding: utf-8 -*-
"""
Create by sandy at 14:04 05/01/2022
Description: ToDo
"""

import django_filters

from apps.projects.api.models import RpcRecord


class RpcRecordFilter(django_filters.FilterSet):
    uid = django_filters.CharFilter(field_name='creator', lookup_expr='id')
    status = django_filters.CharFilter(field_name='status', lookup_expr='icontains')
    start = django_filters.CharFilter(field_name='create_datetime', lookup_expr='gt')
    end = django_filters.CharFilter(field_name='create_datetime', lookup_expr='lt')

    class Meta:
        model = RpcRecord
        fields = ('id', 'creator', 'status', 'create_datetime')

