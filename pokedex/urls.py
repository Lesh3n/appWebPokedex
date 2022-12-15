"""pokedex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from pokemon import views

from api import views as apiView

'''
TODO: Falta poner las urls correspondientes a la api.
'''

urlpatterns = [
    #URL API
    path('api-auth/', include('rest_framework.urls')),
    #path('api-auth/', include('rest_framework.urls')),
    #path('api-auth/', include('rest_framework.urls')),
    #path('api-auth/', include('rest_framework.urls')),
    #URL ADMIN
    path('admin/', admin.site.urls),
    path('', views.listarAgregarPokemon),
    path('eliminarPkmn/<int:id>', views.eliminarPokemon),
    path('actualizarPkmn/<int:id>', views.actualizarPokemon),
    #URLS PokeMart
    path('listadoAgregarProducto/', views.listadoAgregarProducto),
    path('eliminarProducto/<id>', views.eliminarProducto),
    path('actualizarProducto/<id>', views.actualizarProducto),
    #URLS Entrenador 
    path('ListarAgregarEntrenador/', views.listar_agregar_entrenador),
    path('eliminarEntrenador/<id>', views.eliminar_entrenador),
    path('actualizarEntrenador/<id>', views.actualizar_entrenador),

]
