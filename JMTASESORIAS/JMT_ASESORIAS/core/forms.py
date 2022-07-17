from django import forms
from .models import Usuario, Tasacion
#from django.contrib.auth.forms import UserCreationForm


#class UsuarioRegisterForm(UserCreationForm):
 #   email = forms.EmailField()
#    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    
#    class Meta:
#        model = Usuario
 #       fields = '__all__'


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
        
        
        
