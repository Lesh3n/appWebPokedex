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
