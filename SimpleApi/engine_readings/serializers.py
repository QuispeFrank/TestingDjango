from rest_framework import serializers
from .models import Engine, Reading


class ReadingSerializer(serializers.ModelSerializer):
    """
Serializing all the books
"""
    class Meta:
        model = Reading
        fields = ('id','value')

class EngineSerializer(serializers.ModelSerializer):
    """
Serializing all the Authors    
"""
    lecturas = ReadingSerializer(read_only=True, many=True, source="reading_set")

    class Meta:
        model = Engine
        fields = ('id', 'name', 'lecturas')
