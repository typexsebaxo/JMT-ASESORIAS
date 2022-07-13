from django import forms
from .models import Usuario, Tasacion

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
        