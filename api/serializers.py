from rest_framework import serializers
from api.models import Pokemon, Pokemart, Entrenador

class pokemon_serializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        field = '__all__'


class pokemart_serializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemart
        field = '__all__'


class entrenador_serializer(serializers.ModelSerializer):
    class Meta:
        model = Entrenador
        field = '__all__'