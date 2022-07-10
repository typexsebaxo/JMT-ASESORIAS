from django.contrib import admin
from .models import Ciudad, Permiso, Region, Tasacion, Tasador, Usuario
# Register your models here.

admin.site.register(Ciudad)
admin.site.register(Permiso)
admin.site.register(Region)
admin.site.register(Tasacion)
admin.site.register(Tasador)
admin.site.register(Usuario)