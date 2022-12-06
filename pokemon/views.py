from django.shortcuts import redirect, render
from django.http import HttpResponse

#Modelos
from pokemon.models import Pokemon
from pokemon.models import PokeMart
from pokemon.models import Entrenador

#Formularios
from pokemon.forms import formulario_registro_pokemon
from pokemon.forms import FormPokeMart
from pokemon.forms import formulario_registro_entrenador

#Mensajes de error
from django.contrib import messages


def listarAgregarPokemon(request):
    if request.method == 'POST':
        form = formulario_registro_pokemon(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Datos guardados exitosamente")
    form = formulario_registro_pokemon()
    pokemons = Pokemon.objects.all()
    context = {'pokemons' : pokemons, 'form' : form}
    return render(request, 'templatesPokedex/ListarAgregarPokemon.html', context)


def eliminarPokemon(id):
    pokemon = Pokemon.objects.get(id = id)
    pokemon.delete()
    return redirect('/')



def actualizarPokemon(request,id):
    pokemon = Pokemon.objects.get(id = id)
    form = formulario_registro_pokemon(instance=pokemon)
    if request.method == 'POST':
        form = formulario_registro_pokemon(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            messages.success(request, "Datos actualizados exitosamente")
            return redirect('/')
    data = {'form' : form}
    return render(request, 'templatesPokedex/ListarAgregarPokemon.html', data)



'''
Vistas de POKEMART
'''

def listadoAgregarProducto(request):
    form = FormPokeMart()
    if request.method == 'POST':
        form = FormPokeMart(request.POST)
        if form.is_valid():
            form.save()
    form = FormPokeMart()
    pokemart = PokeMart.objects.all()
    context = {'form': form, 'pokemart': pokemart}
    return render(request, 'templatesPokemart/ListarAgregarProductos.html', context)


def eliminarProducto(id):
    productos = PokeMart.objects.get(id=id)
    productos.delete()
    return redirect('/listadoAgregarProducto')


def actualizarProducto(request, id):
    productos = PokeMart.objects.get(id = id)
    form = FormPokeMart(instance=productos)
    if request.method == 'POST':
        form = FormPokeMart(request.POST, instance=productos)
        if form.is_valid():
            form.save()
        return redirect('/listadoAgregarProducto')
    data = {'form': form}
    return render(request, 'templatesPokemart/ListarAgregarProductos.html', data)


'''
View entrenadores
'''

def listar_agregar_entrenador(request):
    if request.method == "POST":
        formulario = formulario_registro_entrenador(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.succes(request, "Entrenador registrado con exito!")
    formulario = formulario_registro_entrenador()
    entrenador = Entrenador.objects.all()
    context = {'formulario': formulario, 'entrenador': entrenador}
    return render(request, 'templateEntrenador/ListarAgregarEntrenador.html', context)


def eliminar_entrenador(id):
    entrenador = Entrenador.objects.get(id = id)
    entrenador.delete()
    #Poner el enlace del archivo urls entre las comillas.
    return redirect('')


def actualizar_entrenador(request, id):
    entrenador = Entrenador.objects.get(id = id)
    formulario = formulario_registro_entrenador(instance = entrenador)
    if request.method == 'POST':
        formulario = formulario_registro_entrenador(request.POST, instance = entrenador)
        if formulario.is_valid():
            formulario.save()
            messages.success('Entrenador actualizado exitosamente!')
        return redirect('/rutaDelTemplate')
    datos = {'formulario': formulario}
    return render(request, 'templateEntrenador/ListarAgregarEntrenador.html', datos)
