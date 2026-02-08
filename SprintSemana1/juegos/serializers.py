from rest_framework import serializers
from .models import Consola

class ConsolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consola
        fields = ['id', 'nombre', 'fabricante', 'generacion', 'activo', 'created_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
        }
