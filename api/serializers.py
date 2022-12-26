from rest_framework import serializers
from api.models import Pokemon, Pokemart, Entrenador

class pokemon_serializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'


class pokemart_serializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemart
        fields = '__all__'


class entrenador_serializer(serializers.ModelSerializer):
    class Meta:
        model = Entrenador
        fields = '__all__'