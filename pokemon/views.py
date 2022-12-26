from django.shortcuts import redirect, render
from django.http import HttpResponse

#Modelos
from api.models import Pokemon, Pokemart, Entrenador


#Formularios
from pokemon.forms import formulario_registro_pokemon, formulario_registro_pokemart, formulario_registro_entrenador


#Mensajes de error
from django.contrib import messages

'''
TODO: EDITAR LAS VIEWS PARA QUE SE COMUNIQUEN CON EL VIEWS DE LA API Y QUE ESTA PUEDA HACER LOS GET
POST, PUT Y DELETE.
'''


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


def eliminarPokemon(request, id):
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
    if request.method == 'POST':
        form = formulario_registro_pokemart(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Datos guardados exitosamente")
    form = formulario_registro_pokemart()
    pokemart = Pokemart.objects.all()
    context = {'form': form, 'pokemart': pokemart}
    return render(request, 'templatesPokemart/ListarAgregarProductos.html', context)


def eliminarProducto(request, id):
    productos = Pokemart.objects.get(id=id)
    productos.delete()
    return redirect('/ListarAgregarProductos')


def actualizarProducto(request, id):
    productos = Pokemart.objects.get(id = id)
    form = formulario_registro_pokemart(instance=productos)
    if request.method == 'POST':
        form = formulario_registro_pokemart(request.POST, instance=productos)
        if form.is_valid():
            form.save()
        return redirect('/ListarAgregarProductos')
    data = {'form': form}
    return render(request, 'templatesPokemart/ListarAgregarProductos.html', data)


'''
View entrenadores
'''

def listar_agregar_entrenador(request):
    if request.method == "POST":
        form = formulario_registro_entrenador(request.POST)
        if form.is_valid():
            form.save()
    form = formulario_registro_entrenador()
    entrenador = Entrenador.objects.all()
    pokemon = Pokemon.objects.all()
    pokemart = Pokemart.objects.all()
    context = {
        'form': form, 
        'entrenador': entrenador,
        'pokemon' : pokemon,
        'pokemart' : pokemart
    }
    return render(request, 'templateEntrenador/ListarAgregarEntrenador.html', context)


def eliminar_entrenador(request, id):
    entrenador = Entrenador.objects.get(id = id)
    entrenador.delete()
    #Poner el enlace del archivo urls entre las comillas.
    return redirect('/ListarAgregarEntrenador')


def actualizar_entrenador(request, id):
    entrenador = Entrenador.objects.get(id = id)
    formulario = formulario_registro_entrenador(instance = entrenador)
    if request.method == 'POST':
        formulario = formulario_registro_entrenador(request.POST, instance = entrenador)
        if formulario.is_valid():
            formulario.save()
        return redirect('/actualizarEntrenador')
    datos = {'formulario': formulario}
    return render(request, 'templateEntrenador/ListarAgregarEntrenador.html', datos)
