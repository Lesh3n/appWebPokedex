from django.db import models

# Create your models here.
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
    nombreObjeto = models.CharField(max_length=50)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    lugar = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    fechaCompra = models.DateField()

#TODO: Hacer el modelo de Entrenador para la inserción de datos, borrado y vista de los datos.
