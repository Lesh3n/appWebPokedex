from django import forms

class formulario_registro_pokemon(forms.Form):
    nombre = forms.CharField()
    tipo = forms.CharField()
    ataque_base_1 = forms.CharField()
    ataque_especial_1 = forms.CharField()
    dano_base = forms.IntegerField()
    defensa_base = forms.IntegerField()


    nombre.widget.attrs['class'] = 'form-control'
    tipo.widget.attrs['class'] = 'form-control'
    ataque_base_1.widget.attrs['class'] = 'form-control'
    ataque_especial_1.widget.attrs['class'] = 'form-control'
    dano_base.widget.attrs['class'] = 'form-control'
    defensa_base.widget.attrs['class'] = 'form-control'