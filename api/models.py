from django.db import models

# Create your models here.
'''

class Pokemon(models.Model)

contiene los siguientes parámetros que son los que se recibirán por medio de un FORM

id = int (AutoIncrementable, no es necesario agregarlo)

nombre = str, tiene un largo de 60 y NO se puede dejar en blanco.

tipo = str, tiene un largo de 40 y NO se puede dejar en blanco.

ataque_base_1 = str, es un ataque de poder base que solo funciona por daño físico. NO es la cantidad total
del pkmn en dato numérico.

ataque_especial_1 = str, ataque especial base que funciona a base de daño mágico.

dano_base = int, daño total base del pkmn en dato numérico.

defensa_base = int, defensa total base del pkmn en dato numérico.

propietario = str, propietario del pkmn. 

'''
class Pokemon(models.Model):
    id = models.AutoField(primary_key=True,blank=False)
    nombre = models.CharField(max_length=60,blank=False)
    tipo = models.CharField(max_length=40,blank=False)
    ataque_base_1 = models.CharField(max_length=70,blank=False)
    ataque_especial_1 = models.CharField(max_length=70,blank=False)
    dano_base = models.IntegerField(blank=False)
    defensa_base = models.IntegerField(blank=False)


'''
Modelo Pokemart
'''
class PokeMart(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    nombreObjeto = models.CharField(max_length=50)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    lugar = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    fechaCompra = models.DateField()



'''
Esta clase, crea la tabla entrenador que contendrá los datos de cada uno de los entrenadores.

class Entrenador(models.Model):
    id = int, es auto incrementable, no requiere de ingreso por parte del usuario.
    nombre = str
    sexo = str
    region = str

    objeto_mas_usado = int, en objeto_mas_usado se mostrará el ID asociado que viene como foreign key desde
    la tabla Pokemart.

    pokemon_favorito = int, se mostrará el ID del pkmn que tendrá asociado el entrenador.

'''
class Entrenador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    Region = models.CharField(max_length=50, blank=False)
    id_objeto_mas_usado = models.ForeignKey(PokeMart, on_delete=models.CASCADE)
    nombre_objeto_mas_usado = models.CharField(max_length=80, blank=False)
    id_pokemon_favorito = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    nombre_pokemon_favorito = models.CharField(max_length=60, blank=False)

