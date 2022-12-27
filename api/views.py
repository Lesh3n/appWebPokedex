from django.shortcuts import render
from .serializers import pokemon_serializer, pokemart_serializer, entrenador_serializer
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

'''
TODO: PONER LAS VIEWS CORRESPONDIENTES A LA API PARA VISUALIZAR CONTENIDOS.
'''

# Create your views here.
class ListaPokemon(APIView):

    def get(self, request):
        pokemons = Pokemon.objects.all()
        serializer = pokemon_serializer(pokemons, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = pokemon_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DetallePokemon(APIView):

    def get_pokemon(self, pk):
        try:
            return Pokemon.objects.get(pk = pk)
        except Pokemon.DoesNotExist:
            return Http404

    def get(self, request, pk):
        pokemon = self.get_pokemon(pk)
        serializer = pokemon_serializer(pokemon)
        return Response(serializer.data)

    def put(self, request, pk):
        pokemon = self.get_pokemon(pk)
        serializer = pokemon_serializer(pokemon, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pokemon = self.get_pokemon(pk)
        pokemon.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class ListaEntrenador(APIView):

    def get(self, request):
        entrenadores = Entrenador.objects.all()
        serializer = entrenador_serializer(entrenadores, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = entrenador_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DetalleEntrenador(APIView):

    def get_entrenador(self, pk):
        try:
            return Entrenador.objects.get(pk = pk)
        except Entrenador.DoesNotExist:
            return Http404

    def get(self, request, pk):
        entrenador = self.get_entrenador(pk)
        serializer = entrenador_serializer(entrenador)
        return Response(serializer.data)

    def put(self, request, pk):
        entrenador = self.get_entrenador(pk)
        serializer = entrenador_serializer(entrenador, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        entrenador = self.get_entrenador(pk)
        entrenador.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class ListaPokemart(APIView):

    def get(self, request):
        objetos = Pokemart.objects.all()
        serializer = pokemart_serializer(objetos, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = pokemart_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DetallePokemart(APIView):

    def get_objeto(self, pk):
        try:
            return Pokemart.objects.get(pk = pk)
        except Pokemart.DoesNotExist:
            return Http404

    def get(self, request, pk):
        objeto = self.get_objeto(pk)
        serializer = pokemart_serializer(objeto)
        return Response(serializer.data)

    def put(self, request, pk):
        objeto = self.get_objeto(pk)
        serializer = pokemart_serializer(objeto, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        objeto = self.get_objeto(pk)
        objeto.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)