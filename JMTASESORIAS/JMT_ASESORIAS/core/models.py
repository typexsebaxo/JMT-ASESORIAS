# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class Ciudad(models.Model):
    nombre = models.CharField(primary_key=True, max_length=50)
    region_nombre = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_nombre')

    class Meta:
        managed = False
        db_table = 'ciudad'
        
    def __str__(self):
        return self.nombre


class Permiso(models.Model):
    rol = models.CharField(primary_key=True, max_length=10)
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'permiso'
        
    def __str__(self):
        return self.rol


class Region(models.Model):
    nombre = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'region'
        
    def __str__(self):
        return self.nombre


class Tasacion(models.Model):
    rut_propietario = models.CharField(primary_key=True, max_length=15)
    propietario = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now = True)
    documentacion = models.BinaryField()
    usuario_nombre = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_nombre')
    tasacion_region = models.ForeignKey(Region, models.DO_NOTHING, db_column='region_nombre')

    class Meta:
        managed = False
        db_table = 'tasacion'
        
    def __str__(self):
        return self.rut_propietario


class Usuario(models.Model):
    nombre = models.CharField(primary_key=True, max_length=50)
    apellido = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=25)
    correo = models.CharField(max_length=30)
    telefono = models.BigIntegerField()
    permiso_rol = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='permiso_rol')
    
    
    class Meta:
        managed = False
        db_table = 'usuario'
        
    def __str__(self):
        return self.nombre    
        

