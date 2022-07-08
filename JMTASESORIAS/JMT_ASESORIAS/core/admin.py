from django.contrib import admin
from .models import Administrador, Ciudad, Permisos, Region, Resumen, Tasacion, Tasador, Usuario
# Register your models here.

admin.site.register(Administrador)
admin.site.register(Ciudad)
admin.site.register(Permisos)
admin.site.register(Region)
admin.site.register(Resumen)
admin.site.register(Tasacion)
admin.site.register(Tasador)
admin.site.register(Usuario)