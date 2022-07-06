from django.db import models

#  Create your models here.



class usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    email = models.CharField(max_length = 150, blank=True, null=True)
    password = models.CharField(max_length = 50, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'usuario'

class admin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nombre_admin = models.CharField(max_length = 50, blank=True, null=True)
    rut_admin = models.CharField(max_length = 10, unique = True, blank=True, null=True)
    correo_admin = models.CharField(max_length = 150, blank=True, null=True)
    telefono_admin = models.IntegerField(("11"), blank=True, null=True)
    ciudad_nombre_ciudad = models.CharField(max_length = 50, blank=True, null=True)
    usuario_id_usuario = models.IntegerField(("11"), blank=True, null=True)
    id_usuario = models.ForeignKey(usuario, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'admin'


class region(models.Model):
    numero_region = models.IntegerField(("11"), blank=True, null=True)
    nombre_region = models.TextField(max_length = 50, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'region'

class  ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length = 50, blank=True, null=True)
    comuna_ciudad = models.CharField(max_length = 50, blank=True, null=True)
    region_numero_region = models.ForeignKey(region, models.DO_NOTHING, db_column='region_numero_region', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ciudad'

class horario_lab(models.Model):
    fecha = models.DateField((""), auto_now=False, auto_now_add=False)
    hora_inicio = models.TimeField(auto_now=False, auto_now_add=False)
    hora_termino = models.TimeField(auto_now=False, auto_now_add=False)
    class Meta:
        managed = False
        db_table = 'horario_lab'

class permisos(models.Model):
    id_permisos = models.AutoField(primary_key=True)
    crear_usuario = models.CharField(max_length = 2, blank=True, null=True)
    modificar_usuario = models.CharField(max_length = 2, blank=True, null=True)
    eliminar_usuario = models.CharField(max_length = 2, blank=True, null=True)
    id_admin = models.ForeignKey(admin, models.DO_NOTHING, db_column='id_admin', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'permisos'

class resumen(models.Model):
    id_resumen = models.AutoField(primary_key=True)
    tasacion_id_tasacion = models.IntegerField(("11"))
    tasador_id_tasador = models.IntegerField(("11"))
    fecha = models.DateField((""), auto_now=False, auto_now_add=False)
    id_admin = models.ForeignKey(admin, models.DO_NOTHING, db_column='id_admin', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'resumen'

class tasacion(models.Model):
    id_tasacion = models.AutoField(primary_key=True)
    rol_propiedad = models.CharField(max_length = 50, blank=True, null=True)
    nombre_propietario = models.CharField(max_length = 50, blank=True, null=True)
    rut_propietario = models.CharField(max_length = 50, blank=True, null=True)
    documentacion = models.CharField(max_length = 50, blank=True, null=True)
    inf_modelo = models.CharField(max_length = 50, blank=True, null=True)
    tasador_id_tasador = models.IntegerField(("11"), blank=True, null=True)
    ciudad_nombre_ciudad = models.CharField(max_length = 50, blank=True, null=True)
    fecha = models.DateField((""), auto_now=False, auto_now_add=False)
    class Meta:
        managed = False
        db_table = 'tasacion'

class tasador(models.Model):
    id_tasador = models.AutoField(primary_key=True)
    nombre_tasador = models.CharField(max_length = 50, blank=True, null=True)
    rut_tasador = models.CharField(max_length = 50, unique=True, blank=True, null=True)
    telefono_tasador = models.IntegerField(("11"), blank=True, null=True)
    correo_tasador = models.CharField(max_length = 150, blank=True, null=True)
    ciudad_nombre_ciudad = models.CharField(max_length = 50, blank=True, null=True)
    usuario_id_usuario = models.IntegerField(("11"), blank=True, null=True)
    horario_lab_fecha = models.DateField((""), auto_now=False, auto_now_add=False)
    id_usuario = models.ForeignKey(usuario, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tasador'
