# -*- coding: utf-8 -*-
"""
Create by sandy at 20:18 24/12/2021
Description: ToDo
"""
import django_filters

from apps.projects.efficiency.models import Efficiency


class EfficiencyFilter(django_filters.FilterSet):
    moduleId = django_filters.CharFilter(field_name='module', lookup_expr='id')
    parentId = django_filters.CharFilter(field_name='module', lookup_expr='id')
    status = django_filters.CharFilter(field_name='status', lookup_expr='icontains')
    creator = django_filters.CharFilter(field_name='creator', lookup_expr='id')
    start = django_filters.CharFilter(field_name='create_datetime', lookup_expr='gt')
    end = django_filters.CharFilter(field_name='create_datetime', lookup_expr='lt')

    class Meta:
        model = Efficiency
        fields = ('id', 'creator', 'status', 'create_datetime')
