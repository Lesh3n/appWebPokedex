from django.contrib import admin
from pokemon.models import Pokemon
#Esta clase sirve para mostrar los pokémon en la interfaz de Django Admin
class PokemonAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','tipo','ataque_base_1','ataque_especial_1','dano_base','defensa_base']

# Register your models here.
admin.site.register(Pokemon, PokemonAdmin)
