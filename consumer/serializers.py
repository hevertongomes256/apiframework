from dataclasses import fields
from rest_framework import serializers
from rest_framework.serializers import IntegerField, CharField
from drf_api_logger.models import APILogsModel


class UserSerializer(serializers.Serializer):
    id = IntegerField()
    title = CharField()

    class Meta:
        fields = ['id', 'title']


class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = APILogsModel
        fields = '__all__'