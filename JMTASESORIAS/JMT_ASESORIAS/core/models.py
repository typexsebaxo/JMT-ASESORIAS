from django.db import models

# Create your models here.
class admin(models.Model):
    id_admin = models.IntegerField(_("11"))
    nombre_admin = models.TextField(max_length = 50)
    rut_admin = models.TextField(max_length = 10)
    correo_admin = models.TextField(max_length = 150)
    telefono_admin = models.IntegerField(_("11"))
    ciudad_nombre_ciudad = models.TextField(max_length = 50)
    usuario_id_usuario = models.IntegerField(_("11"))
    id_usuario = models.IntegerField(_("11"))

class  ciudad(models.Model):
    nombre_ciudad = models.TextField(max_length = 50)
    comuna_ciudad = models.TextField(max_length = 50)
    region_numero_region = models.IntegerField(_("11"))

class horario_lab(models.Model):
    fecha = models.DateField(_(""), auto_now=False, auto_now_add=False)
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()

class permisos(models.Model):
    id_permisos = models.IntegerField(_("11"))
    crear_usuario = models.TextField(max_length = 2)
    modificar_usuario = models.TextField(max_length = 2)
    eliminar_usuario = models.TextField(max_length = 2)
    id_admin = models.IntegerField(_("11"))

class region(models.Model):
    numero_region = models.IntegerField(_("11"))
    nombre_region = models.TextField(max_length = 50)

class resumen(models.Model):
    id_resumen = models.IntegerField(_("11"))
    tasacion_id_tasacion = models.IntegerField(_("11"))
    tasador_id_tasador = models.IntegerField(_("11"))
    fecha = models.DateField(_(""), auto_now=False, auto_now_add=False)
    id_admin = models.IntegerField(_("11"))

class tasacion(models.Model):
    id_tasacion = models.IntegerField(_("11"))
    rol_propiedad = models.TextField(max_length = 50)
    nombre_propietario = models.TextField(max_length = 50)
    rut_propietario = models.TextField(max_length = 50)
    documentacion = models.BinaryField()
    inf_modelo = models.BinaryField()
    tasador_id_tasador = models.IntegerField(_("11"))
    ciudad_nombre_ciudad = models.TextField(max_length = 50)
    fecha = models.DateField(_(""), auto_now=False, auto_now_add=False)

class tasador(models.Model):
    id_tasador = models.IntegerField(_("11"))
    nombre_tasador = models.TextField(max_length = 50)
    rut_tasador = models.TextField(max_length = 50)
    telefono_tasador = models.IntegerField(_("11"))
    correo_tasador = models.TextField(max_length = 150)
    ciudad_nombre_ciudad = models.TextField(max_length = 50)
    usuario_id_usuario = models.IntegerField(_("11"))
    horario_lab_fecha = models.DateField(_(""), auto_now=False, auto_now_add=False)
    id_usuario = models.IntegerField(_("11"))

class usuario(models.Model):
    id_usuario = models.IntegerField(_("11"))
    email = models.TextField(max_length = 150)
    password = models.TextField(max_length = 50)