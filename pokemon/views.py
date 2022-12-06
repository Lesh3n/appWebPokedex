from django.shortcuts import redirect, render
from django.http import HttpResponse

#Modelos
from pokemon.models import Pokemon
from pokemon.models import PokeMart

#Formularios
from . import forms
from pokemon.forms import formulario_registro_pokemon
from pokemon.forms import FormPokeMart

#Mensajes de error
from django.contrib import messages

# Create your views here.fffff
'''
Esto sirvio en un inicio para probar si la web funcionaba correctamente.
'''
#def display(request):
#    return HttpResponse("<h1>Estás en el registro de PKMN's</h1>")



'''
Aquí va el render de la lista de Pokemons, también el render del actualizar, borrar e ingresar datos
'''

#Este era el "index"
'''def renderListaPkmn(request):
    return render(request, 'templatesPokedex/listarPkmn.html')'''

#Esta es la lista. (No se va a usar)
'''def datosPokemon(request):
    pokemons = Pokemon.objects.all()
    data = {'pokemons' : pokemons}
    return render(request, 'templatesPokedex/listarPkmn.html', data)'''''


#Este tiene que ser modificado para que tener el form junto a la tabla
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

#Ta Joya
def eliminarPokemon(request, id):
    pokemon = Pokemon.objects.get(id = id)
    pokemon.delete()
    return redirect('/')


#Ta Joya
def actualizarPokemon(request,id):
    pokemon = Pokemon.objects.get(id = id)
    form = formulario_registro_pokemon(instance=pokemon)
    if request.method == 'POST':
        form = formulario_registro_pokemon(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            messages.success(request, "Datos actualizados exitosamente")
            return redirect('/')
        #return render(request, 'templatesPokedex/listarPkmn.html')
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


def eliminarProducto(request, id):
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