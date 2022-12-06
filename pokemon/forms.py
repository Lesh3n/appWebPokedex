from django import forms
from pokemon.models import Pokemon
from pokemon.models import PokeMart
from pokemon.models import Entrenador

#Formulario hecho.

'''
Esta clase genera el formulario de registro de los pokemon. Al inicio de esta, se declaran las variables de los campos junto con su tipo de dato.
En la sub-clase Meta, se recibe el modelo de la BDD y luego se definen los campos en los que se escribiran los datos.
'''


class formulario_registro_pokemon(forms.ModelForm):
    nombre = forms.CharField()
    tipo = forms.CharField()
    ataque_base_1 = forms.CharField()
    ataque_especial_1 = forms.CharField()
    dano_base = forms.IntegerField()
    defensa_base = forms.IntegerField()

    class Meta:
        model = Pokemon
        fields = ['nombre','tipo','ataque_base_1','ataque_especial_1','dano_base','defensa_base']

    def clean_nombre(self):
        input_nombre = self.cleaned_data['nombre']
        if len(input_nombre) < 1:
            raise forms.ValidationError("No se ha ingresado un nombre de Pokemon!")
        return input_nombre

    def clean_tipo(self):
        input_tipo = self.cleaned_data['tipo']
        if len(input_tipo) < 1:
            raise forms.ValidationError("No se ha ingresado un tipo de Pokemon!")
        return input_tipo


    nombre.widget.attrs['class'] = 'form-control'
    tipo.widget.attrs['class'] = 'form-control'
    ataque_base_1.widget.attrs['class'] = 'form-control'
    ataque_especial_1.widget.attrs['class'] = 'form-control'
    dano_base.widget.attrs['class'] = 'form-control'
    defensa_base.widget.attrs['class'] = 'form-control'

    

        


    '''
    def clean(self):
        user_clean_data = super().clean()

        input_nombre = user_clean_data['nombre']
        if len(input_nombre) < 1:
            raise forms.ValidationError("Campo 'Nombre' vacio.")

    '''


'''
Formulario de PokeMart
'''
class FormPokeMart(forms.ModelForm):
    nombreObjeto = forms.CharField(min_length=3, max_length=50)
    precio = forms.IntegerField(min_value=1, max_value=100000)
    cantidad = forms.IntegerField(min_value=1, max_value=100000)
    lugar = forms.CharField(min_length=3, max_length=50)
    tipo = forms.CharField(min_length=3, max_length=50)
    fechaCompra = forms.DateField()

    class Meta:
        model = PokeMart
        fields = '__all__'



class formulario_registro_entrenador(forms.ModelForm):
    nombre = forms.CharField(max_length=50)
    sexo = forms.CharField(max_length=1)
    region = forms.CharField(max_length=50)
    objeto_mas_usado = forms.IntegerField()
    pokemon_favorito = forms.IntegerField()

    class Meta:
        model = Entrenador
        fields = ['nombre','sexo','region','objeto_mas_usado','pokemon_favorito']

    nombre.widget.attrs['class'] = 'form-control'
    sexo.widget.attrs['class'] = 'form-control'
    region.widget.attrs['class'] = 'form-control'
    objeto_mas_usado.widget.attrs['class'] = 'form-control'
    pokemon_favorito.widget.attrs['class'] = 'form-control'
