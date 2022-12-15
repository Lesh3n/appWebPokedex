from django.contrib import admin
from api.models import Pokemon, PokeMart, Entrenador

#Esta clase sirve para mostrar los pokémon en la interfaz de Django Admin
class PokemonAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','tipo','ataque_base_1','ataque_especial_1','dano_base','defensa_base']

class pokemartAdmin(admin.ModelAdmin):
    list_display = ['id','nombreObjeto', 'precio', 'cantidad', 'lugar', 'tipo', 'fechaCompra']

class entrenadorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'sexo', 'Region', 'nombre_objeto_mas_usado', 'nombre_pokemon_favorito']


# Register your models here.
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokeMart, pokemartAdmin)
admin.site.register(Entrenador, entrenadorAdmin)
