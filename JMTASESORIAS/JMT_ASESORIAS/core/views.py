from django.shortcuts import render

# Create your views here.

def InicioSesion(request):
 return render(request,"core/InicioSesion.html")