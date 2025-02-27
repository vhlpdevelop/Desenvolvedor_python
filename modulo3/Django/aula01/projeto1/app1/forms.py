from django import forms
from .models import User

#Formularios
#modelForm e form.Form, cada um é diferente

#modelForm
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'telefone', 'email']

#form.Form
