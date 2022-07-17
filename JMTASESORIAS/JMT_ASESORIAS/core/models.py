# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import random
import string

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))



class CustomAccountManager(BaseUserManager):
    def create_user(self, correo, nombre, apellido, contrasena, **other_fields):

        if not correo:
            raise ValueError(_('You must provide an email address'))

        correo = self.normalize_correo(correo)
        user = self.model(correo=correo, nombre=nombre,
                          apellido=apellido, **other_fields)
        user.set_password(contrasena)
        user.save()
        return user

    def create_superuser(self, correo, nombre, apellido, contrasena, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(correo, nombre, apellido, contrasena, **other_fields)
    
    


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


class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(primary_key=True, max_length=50)
    apellido = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=25)
    correo = models.EmailField(_('email address'), unique=True)
    telefono = models.BigIntegerField()
    permiso_rol = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='permiso_rol')
    slug = models.SlugField(max_length=255, unique=True)
    
    register_date = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    objects = CustomAccountManager()
    
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['contrasena', 'apellido']
    
    class Meta:
        managed = False
        db_table = 'usuario'
        
    def __str__(self):
        return f'{self.contrasena} {self.apellido}'
    
    def get_absolute_url(self):
        return reverse('usuarios:menutasador', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.correo)
        super(Usuario, self).save(*args, **kwargs)
