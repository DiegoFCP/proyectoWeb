from django import forms
from .models import Usuario, Producto

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'