from django.urls import path, include
from .views import InicioSesion, Menuadmin, Admintasador, Menutasacionadmin, Graficostasacion, Notificacionesadmin, Creatasador, Menutasador, Misproyectos, Agregar_usuario

urlpatterns = [
    #path('admin/', admin.site.urls), 
    path('', InicioSesion, name='InicioSesion'),
    path('menuadmin/', Menuadmin, name='menuadmin'),
    path('admintasador/', Admintasador, name='admintasador'),
    path('menutasacionadmin/', Menutasacionadmin, name='menutasacionadmin'),
    path('graficostasacion/', Graficostasacion, name='graficostasacion'),
    path('notificacionesadmin/', Notificacionesadmin, name='notificacionesadmin'),
    path('creatasador/', Creatasador, name='creatasador'),
    path('menutasador/', Menutasador, name='menutasador'),
    path('misproyectos/', Misproyectos, name='misproyectos'),
    path('agregar-tasador/',  Agregar_usuario, name='agregar_usuario'),
]