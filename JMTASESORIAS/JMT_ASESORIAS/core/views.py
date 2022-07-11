from django.shortcuts import render
from django.http import Http404
from django.utils import html
from django.http import HttpResponse
from django.db import connection
import cx_Oracle
from .forms import UsuarioForm

# Create your views here.

def InicioSesion(request):
 return render(request,"core/InicioSesion.html")

def Menuadmin(request):
    data = {
        'usuarios':listado_usuario()
    }
    return render(request,"core/menuadmin.html", data)

def Admintasador(request):
    #print(listado_usuario())    #ESTO ES PARA MOSTRAR EN EL TERMINAL LAS FILAS DE LA TABLA USUARIO
    
    data = {
        'usuarios':listado_usuario()
    }
    
    return render(request,"core/admintasador.html", data)

def Menutasacionadmin(request):
    return render(request,"core/menutasacionadmin.html")

def Graficostasacion(request):
    return render(request,"core/graficostasacion.html")

def Notificacionesadmin(request):
    return render(request,"core/notificacionesadmin.html")

def Creatasador(request):
    data = {
        'regiones':Listar_regiones(),
    }
    
    
    if request.method == 'POST':
        correo = request.POST.get('email')
        contrasena = request.POST.get('password')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        region_id = request.POST.get('region')
        telefono = request.POST.get('telefono')
        salida = agregar_tasador(correo, contrasena, nombre, apellido, region_id, telefono)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
        else:
            data['mensaje'] = 'no se ha podido guardar'
    
    return render(request,"core/creatasador.html", data)

def Menutasador(request):
    return render(request,"core/menutasador.html")
    
def Misproyectos(request):
    return render(request,"core/misproyectos.html")


def listado_usuario():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("SP_LISTAR_USUARIO", [out_cur])
    
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista 

def Listar_regiones():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("SP_LISTAR_REGIONESS", [out_cur])
    
    lista = [] 
    for fila in out_cur:
        lista.append(fila)
    return lista    

def agregar_tasador(correo, contrasena, nombre, apellido, region_id, telefono):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_TASADOR',[correo, contrasena, nombre, apellido, region_id, telefono, salida])
    return salida.getvalue()

def Agregar_usuario(request):
    
    data = {
        'form':UsuarioForm()
    }
    
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "Guardado correctamente"
        else:
            data["form"] = formulario
    
    return render(request, "core/usuario/agregar.html", data)