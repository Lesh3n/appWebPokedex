from django.shortcuts import redirect, render
from django.http import HttpResponse
from pokemon.models import Pokemon
from . import forms
from pokemon.forms import formulario_registro_pokemon
from django.contrib import messages
# Create your views here.fffff
'''
Esto sirvio en un inicio para probar si la web funcionaba correctamente.
'''
#def display(request):
#    return HttpResponse("<h1>Estás en el registro de PKMN's</h1>")

'''
--------------------------------------------------------------------------------------------------------
TODO: Cambiar nombres a variables que son confusos a simple vista, se requiere a cambiar lo sgte,
1.- Nombre a template de registroPkmn por "listaPkmn"
2.- Cambiar el template del archivo views.py y de urls.py

---------------------------------------------------------------------------------------------------------
'''







def renderListaPkmn(request):
    return render(request, 'templatesPokedex/listarPkmn.html')


def datosPokemon(request):
    pokemons = Pokemon.objects.all()
    data = {'pokemons' : pokemons}
    return render(request, 'templatesPokedex/listarPkmn.html', data)


def agregarPokemon(request):
    form = forms.formulario_registro_pokemon()
    if request.method == 'POST':
        form = forms.formulario_registro_pokemon(request.POST)
        if form.is_valid():
            form.save()
            '''
            Es como la forma mas "arcaica" de ingresar los datos, pero, al hacer esto no se puede hacer lo de eliminar y actualizar datos no se pq.
            '''
            #nombre = form.cleaned_data['nombre']
            #tipo = form.cleaned_data['tipo']
            #ataque_base = form.cleaned_data['ataque_base_1']
            #ataque_especial = form.cleaned_data['ataque_especial_1']
            #dano_base = form.cleaned_data['dano_base']
            #defensa_base = form.cleaned_data['defensa_base']
            '''
            Se debe de poner el nombre del campo que esta presente en el model para luego poder ingresar la variable que recupera el dato ingresado por el usuario
            '''
            #Pokemon.objects.create(nombre=nombre,tipo=tipo,ataque_base_1=ataque_base,ataque_especial_1=ataque_especial,dano_base=dano_base,defensa_base=defensa_base)
            messages.success(request, "Datos ingresados exitosamente")
            return datosPokemon(request)
        else:
            form = formulario_registro_pokemon()

    data = {'form' : form}
    return render(request, 'templatesPokedex/ingresoPkmn.html', data)



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
        #return render(request, 'templatesPokedex/listarPkmn.html')
        else:
            form = formulario_registro_pokemon()
    data = {'form' : form}
    return render(request, 'templatesPokedex/ingresoPkmn.html', data)


