# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey('Region', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ciudad'

    def __str__(self):
        return self.nombre


class Permiso(models.Model):
    id = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'permiso'
        
    def __str__(self):
        return self.rol


class Region(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'region'
        
    def __str__(self):
        return self.nombre


class Tasacion(models.Model):
    id = models.AutoField(primary_key=True)
    propiedad = models.CharField(max_length=50)
    nombre_propietario = models.CharField(max_length=50)
    rut_propietario = models.CharField(max_length=50)
    documentacion = models.BinaryField()
    fecha = models.DateField()
    tasador = models.ForeignKey('Tasador', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tasacion'
        
    def __str__(self):
        return self.propiedad


class Tasador(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tasador'
        
    def __str__(self):
        return self.usuario


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=25)
    correo = models.CharField(max_length=30)
    telefono = models.FloatField()
    permiso = models.ForeignKey(Permiso, models.DO_NOTHING)
    region = models.ForeignKey(Region, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return self.nombre