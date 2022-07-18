from django.shortcuts import render, redirect
from django.db import connection
import cx_Oracle
from .models import *
from .forms import UsuarioForm, TasacionForm
from django.core.files.storage import FileSystemStorage

# Create your views here.



def InicioSesion(request):
    
    data = {
        'permisos':listar_permiso()
    }
    
    
    return render(request,"core/iniciosesion.html", data)

def InicioSession(request):
    
    data = {
        'permisos':listar_permiso()
    }
    
    return render(request,"core/iniciosesion.html", data)

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
    data = {
        'tasaciones':listado_tasacion()
    }
    return render(request,"core/menutasacionadmin.html", data)

def Menutasaciontasador(request):
    data = {
        'tasaciones':listado_tasacion()
    }
    return render(request,"core/tasaciontasador.html", data)

def Graficostasacion(request):
    return render(request,"core/graficostasacion.html")

def Notificacionesadmin(request):
    return render(request,"core/notificacionesadmin.html")

def Notificacionestasador(request):
    return render(request,"core/notificacionestasador.html")


def Newtasacion(request):
    
    data = {
        'form':TasacionForm()
    }
    
    if request.method == 'POST':
        formulario = TasacionForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/tasaciones-tasador/') # para direccionarlo a la views
            #messages.success(request, "Nueva tasacion ingresada")
            data["mensaje"]= "Guardado correctamente"
        else:
            data["form"] = formulario
        return redirect('/tasaciones-tasador/')  # para direccionarlo a la views  
    
    return render(request,"core/newtasacion.html",data)


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
        return redirect('/admintasador/') 
    
    return render(request, "core/usuario/agregar.html", data)

def Creatasador(request):
    data = {
        'regiones':Listar_regiones(),
        'permisos':Listar_permisos(),
    }
    
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('email')
        contrasena = request.POST.get('password')
        permiso_rol = request.POST.get('permiso')
        region_nombre = request.POST.get('region')
        
        salida = agregar_tasador(nombre, apellido, telefono, correo, contrasena, permiso_rol, region_nombre)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
        else:
            data['mensaje'] = 'no se ha podido guardar'
    
    return render(request,"core/creatasador.html", data)

def Menutasador(request):
    return render(request,"core/menutasador.html")
    
def Misproyectos(request):
    return render(request,"core/misproyectos.html")

def Casaz(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/casas/casaz.html', {
            'uploaded_file_url': uploaded_file_url
            })
    return render(request,"core/casas/casaz.html")

def Casapa(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/casas/casapa.html', {
            'uploaded_file_url': uploaded_file_url
            })
    return render(request,"core/casas/casapa.html")

def CasaDina(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/casas/casadinamarca.html', {
            'uploaded_file_url': uploaded_file_url
            })
    return render(request,"core/casas/casadinamarca.html")

def CasaArn01(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/casas/casaarn01.html', {
            'uploaded_file_url': uploaded_file_url
            })
    return render(request,"core/casas/casaarn01.html")

def Misproyectos(request):
    return render(request,"core/misproyectos.html")


def listar_permiso():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("SP_LISTAR_PERMISOS", [out_cur])
    
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista 


def listado_usuario():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("SP_LISTAR_USUARIO", [out_cur])
    
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista 

def listado_tasacion():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("SP_LISTAR_TASACION", [out_cur])
    
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

def Listar_permisos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("SP_LISTAR_PERMISOS", [out_cur])
    
    lista = [] 
    for fila in out_cur:
        lista.append(fila)
    return lista  

def agregar_tasador(nombre, apellido, telefono, correo, contrasena, permiso_rol, region_nombre):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_TASADOR',[nombre, apellido, telefono, correo, contrasena, permiso_rol, region_nombre, salida])
    return salida.getvalue()


