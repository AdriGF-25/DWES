from rest_framework import serializers
from .models import Consola, Juego

class ConsolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consola
        fields = ['id', 'nombre', 'fabricante']
        extra_kwargs = {'id': {'read_only': True}}

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = '__all__'

class JuegoCreateSerializer(serializers.ModelSerializer):
    consola = serializers.PrimaryKeyRelatedField(queryset=Consola.objects.all())
    class Meta:
        model = Juego
        fields = '__all__'
