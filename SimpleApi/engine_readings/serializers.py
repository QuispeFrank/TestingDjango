from rest_framework import serializers
from .models import Engine, Reading


class ReadingSerializer(serializers.ModelSerializer):
    """
Serializing all the books
"""
    class Meta:
        model = Reading
        fields = ('id','MagV1','MagV2','MagV3')

class EngineSerializer(serializers.ModelSerializer):
    """
Serializing all the Authors    
"""
    lecturas = ReadingSerializer(read_only=True, many=True, source="reading_set")

    class Meta:
        model = Engine
        fields = ('id', 'name', 'lecturas')
