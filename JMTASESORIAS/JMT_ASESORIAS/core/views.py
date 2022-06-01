from django.shortcuts import render
from django.http import Http404
from django.utils import html

# Create your views here.

def InicioSesion(request):
 return render(request,"core/InicioSesion.html")

def Menuadmin(request):
 return render(request,"core/menuadmin.html")

def Admintasador(request):
    return render(request,"core/admintasador.html")

def Menutasacionadmin(request):
    return render(request,"core/menutasacionadmin.html")