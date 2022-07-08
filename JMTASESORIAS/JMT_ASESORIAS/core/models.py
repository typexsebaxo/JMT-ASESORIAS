# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Administrador(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nombre_admin = models.CharField(max_length=50)
    rut_admin = models.CharField(max_length=10)
    correo_admin = models.CharField(max_length=150)
    telefono_admin = models.BigIntegerField()
    ciudad_nombre_ciudad = models.ForeignKey('Ciudad', models.DO_NOTHING, db_column='ciudad_nombre_ciudad')
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_id_usuario')
    id_usuario = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'administrador'


class Ciudad(models.Model):
    nombre_ciudad = models.CharField(primary_key=True, max_length=50)
    comuna_ciudad = models.CharField(max_length=50)
    region_numero_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_numero_region')

    class Meta:
        managed = False
        db_table = 'ciudad'


class Permisos(models.Model):
    id_permisos = models.BigIntegerField(primary_key=True)
    crear_usuario = models.CharField(max_length=2)
    modificar_usuario = models.CharField(max_length=2)
    eliminar_usuario = models.CharField(max_length=2)
    id_admin = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='id_admin')

    class Meta:
        managed = False
        db_table = 'permisos'


class Region(models.Model):
    numero_region = models.BigIntegerField(primary_key=True)
    nombre_region = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'region'


class Resumen(models.Model):
    id_resumen = models.BigIntegerField(primary_key=True)
    tasacion_id_tasacion = models.ForeignKey('Tasacion', models.DO_NOTHING, db_column='tasacion_id_tasacion')
    tasador_id_tasador = models.ForeignKey('Tasador', models.DO_NOTHING, db_column='tasador_id_tasador')
    fecha = models.DateField()
    id_admin = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='id_admin')

    class Meta:
        managed = False
        db_table = 'resumen'


class Tasacion(models.Model):
    id_tasacion = models.AutoField(primary_key=True)
    rol_propiedad = models.CharField(max_length=50)
    nombre_propietario = models.CharField(max_length=50)
    rut_propietario = models.CharField(max_length=10)
    documentacion = models.BinaryField()
    inf_modelo = models.BinaryField()
    tasador_id_tasador = models.ForeignKey('Tasador', models.DO_NOTHING, db_column='tasador_id_tasador')
    ciudad_nombre_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_nombre_ciudad')
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'tasacion'


class Tasador(models.Model):
    id_tasador = models.AutoField(primary_key=True)
    nombre_tasador = models.CharField(max_length=50)
    rut_tasador = models.CharField(max_length=10)
    telefono_tasador = models.BigIntegerField()
    correo_tasador = models.CharField(max_length=150)
    ciudad_nombre_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_nombre_ciudad')
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_id_usuario')
    horario_lab_fecha = models.DateField()
    id_usuario = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tasador'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'usuario'
