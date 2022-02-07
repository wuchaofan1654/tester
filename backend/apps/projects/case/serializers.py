# encoding: utf-8

from rest_framework import serializers
from apps.projects.case import models


class SuiteSerializer(serializers.ModelSerializer):
    create_datetime = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = models.Suite
        fields = '__all__'


class CaseSerializer(serializers.ModelSerializer):
    create_datetime = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = models.Case
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):
    create_datetime = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = models.Record
        fields = '__all__'
