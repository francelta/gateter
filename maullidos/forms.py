from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Maullido

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'password1', 'password2')

class MaullidoForm(forms.ModelForm):
    class Meta:
        model = Maullido
        fields = ['contenido']

    contenido = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 60}))

