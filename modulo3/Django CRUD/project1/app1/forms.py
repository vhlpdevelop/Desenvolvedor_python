from django import forms
from .models import User, Calculo

#Formularios
#modelForm e form.Form, cada um é diferente

#modelForm
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'telefone', 'email']

#form.Form
class CalculoForm(forms.ModelForm):
    class Meta:
        model = Calculo
        fields = ['a', 'b', 'c']