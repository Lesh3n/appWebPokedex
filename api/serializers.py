from rest_framework import serializers
from api.models import Pokemon, PokeMart, Entrenador

class pokemon_serializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        field = '__all__'


class pokemart_serializer(serializers.ModelSerializer):
    class Meta:
        model = PokeMart
        field = '__all__'


class entrenador_serializer(serializers.ModelSerializer):
    class Meta:
        model = Entrenador
        field = '__all__'