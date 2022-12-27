from urllib import request
from django import forms
from api.models import Pokemon, Pokemart, Entrenador



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
        if input_nombre != str(input_nombre):
            raise forms.ValidationError("El tipo de dato ingresado no corresponde a lo pedido!")
        return input_nombre

    def clean_tipo(self):
        input_tipo = self.cleaned_data['tipo']
        if len(input_tipo) < 1:
            raise forms.ValidationError("No se ha ingresado un tipo de Pokemon!")
        if input_tipo != str(input_tipo):
            raise forms.ValidationError("El tipo de dato ingresado no corresponde a lo pedido!")
        return input_tipo

    def clean_ataque_base_1(self):
        input_ataque_base_1 = self.cleaned_data['ataque_base_1']
        if len(input_ataque_base_1) < 1:
            raise forms.ValidationError("No se ha ingresado un poder de ataque base!")
        if input_ataque_base_1 != str(input_ataque_base_1):
            raise forms.ValidationError("Solo te estoy pidiendo el ataque NO el daño de ataque...")
        return input_ataque_base_1

    def clean_ataque_especial_1(self):
        input_ataque_especial_1 = self.cleaned_data['ataque_especial_1']
        if len(input_ataque_especial_1) < 1:
            raise forms.ValidationError("No se ha ingresado un poder de ataque especial!")
        if input_ataque_especial_1 != str(input_ataque_especial_1):
            raise forms.ValidationError("Solo te estoy pidiendo el ataque especial NO el daño NUMERICO de ataque...")
        return input_ataque_especial_1

    def clean_dano_base(self):
        input_dano_base = self.cleaned_data['dano_base']
        if input_dano_base != int(input_dano_base):
            raise forms.ValidationError("Te estoy pidiendo el daño en números, no letras -_-")
        return input_dano_base

    def clean_defensa_base(self):
        input_defensa_base = self.cleaned_data['defensa_base']
        if input_defensa_base != int(input_defensa_base):
            raise forms.ValidationError("Te estoy pidiendo la defensa en números, no letras -_-")
        return input_defensa_base


    nombre.widget.attrs['class'] = 'form-control'
    tipo.widget.attrs['class'] = 'form-control'
    ataque_base_1.widget.attrs['class'] = 'form-control'
    ataque_especial_1.widget.attrs['class'] = 'form-control'
    dano_base.widget.attrs['class'] = 'form-control'
    defensa_base.widget.attrs['class'] = 'form-control'

    

        


    '''
    Esto es para otras validaciones jejeje
    def clean(self):
        user_clean_data = super().clean()

        input_nombre = user_clean_data['nombre']
        if len(input_nombre) < 1:
            raise forms.ValidationError("Campo 'Nombre' vacio.")

    '''


'''
Formulario de PokeMart
'''
class formulario_registro_pokemart(forms.ModelForm):
    nombre_objeto = forms.CharField(min_length=3, max_length=50)
    precio = forms.IntegerField(min_value=1, max_value=100000)
    cantidad = forms.IntegerField(min_value=1, max_value=100000)
    lugar = forms.CharField(min_length=3, max_length=50)
    tipo = forms.CharField(min_length=3, max_length=50)
    fecha_compra = forms.DateField()

    class Meta:
        model = Pokemart
        fields = '__all__'

    def clean_nombre(self):
        input_nombre = self.cleaned_data['nombre_objeto']
        if len(input_nombre) < 1:
            raise forms.ValidationError("No se ha ingresado un nombre de Pokemon!")
        if input_nombre != str(input_nombre):
            raise forms.ValidationError("El tipo de dato ingresado no corresponde a lo pedido!")
        return input_nombre

    def clean_precio(self):
        input_precio = self.cleaned_data['precio']
        if input_precio != int(input_precio):
            raise forms.ValidationError("El tipo de dato ingresado no corresponde a lo pedido!")
        return input_precio

    def clean_cantidad(self):
        input_cantidad = self.cleaned_data['cantidad']
        if input_cantidad != str(input_cantidad):
            raise forms.ValidationError("Tipo de dato incorrecto, se espera un dato numerico.")
        return input_cantidad







class formulario_registro_entrenador(forms.ModelForm):
    nombre = forms.CharField(max_length=50)
    sexo = forms.CharField(max_length=1)
    region = forms.CharField(max_length=50)
    id_pokemon_favorito = Pokemon(id)
    nombre_pokemon_favorito = Pokemon(nombre)
    id_objeto_mas_usado = Pokemart(id)
    

    class Meta:
        model = Entrenador
        fields = ['nombre','sexo','region','id_pokemon_favorito','id_objeto_mas_usado']
        
    nombre.widget.attrs['class'] = 'form-control'
    sexo.widget.attrs['class'] = 'form-control'
    region.widget.attrs['class'] = 'form-control'
