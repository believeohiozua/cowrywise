from rest_framework import serializers
from .models import UuidGenerator


class UuidGeneratorSerializer(serializers.ModelSerializer):
    """UuidGenerator Serializer"""
    class Meta:
        model = UuidGenerator
        fields = '__all__'
