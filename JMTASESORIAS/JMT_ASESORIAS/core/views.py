from django.shortcuts import render
from django.http import Http404
from django.utils import html
from django.http import HttpResponse


# Create your views here.

def InicioSesion(request):
 return render(request,"core/InicioSesion.html")

def Menuadmin(request):
 return render(request,"core/menuadmin.html")

def Admintasador(request):
    return render(request,"core/admintasador.html")

def Menutasacionadmin(request):
    return render(request,"core/menutasacionadmin.html")

def Graficostasacion(request):
    return render(request,"core/graficostasacion.html")

def Notificacionesadmin(request):
    return render(request,"core/notificacionesadmin.html")

def Creatasador(request):
    return render(request,"core/creatasador.html")