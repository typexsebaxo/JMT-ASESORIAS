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
    data = {
        'tasaciones':listado_tasacion()
    }
    return render(request,"core/menutasacionadmin.html", data)

def Graficostasacion(request):
    return render(request,"core/graficostasacion.html")

def Notificacionesadmin(request):
    return render(request,"core/notificacionesadmin.html")

def Newtasacion(request):
    return render(request,"core/newtasacion.html")

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
    return render(request,"core/casaz.html")

def Casapa(request):
    return render(request,"core/casapa.html")

def CasaArn01(request):
    return render(request,"core/casadinamarca.html")

def CasaDina(request):
    return render(request,"core/casaarn01.html")


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



#def loginAction(request):
    #print "Its workjing"
    #if request.method == 'POST' and 'loginButton' in request.POST:
    #    email = request.POST.get('email')
    #    password = request.POST.get('password')

        #print email, password

    #return HttpResponse(json.dumps({}),content_type="application/json")