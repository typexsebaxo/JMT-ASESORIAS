from django import forms
from .models import Usuario, Tasacion, Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = '__all__'
        
        
class TasacionForm(forms.ModelForm):
    
    class Meta:
        model = Tasacion
        fields = '__all__'
        
        widgets = {
            "fecha" : forms.SelectDateWidget()
        }
        
