from rest_framework import serializers
from rest_framework.serializers import IntegerField, CharField


class UserSerializer(serializers.Serializer):
    id = IntegerField()
    title = CharField()

    class Meta:
        fields = ['id', 'title']
