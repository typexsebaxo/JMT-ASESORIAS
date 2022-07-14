from django.urls import path
from django.conf import settings
from .views import InicioSesion, Menuadmin, Admintasador, Menutasacionadmin, Graficostasacion, Notificacionesadmin, Creatasador, Menutasador, Misproyectos, Agregar_usuario, Casaz, Casapa, CasaArn01, CasaDina, Newtasacion

urlpatterns = [
    path('', InicioSesion, name='iniciosesion'),
    #path('login/', loginAction, name='loginAction'),
    path('menuadmin/', Menuadmin, name='menuadmin'),
    path('admintasador/', Admintasador, name='admintasador'),
    path('menutasacion/', Menutasacionadmin, name='menutasacionadmin'),
    path('graficostasacion/', Graficostasacion, name='graficostasacion'),
    path('notificacionesadmin/', Notificacionesadmin, name='notificacionesadmin'),
    path('creatasador/', Creatasador, name='creatasador'),
    path('menutasador/', Menutasador, name='menutasador'),
    path('misproyectos/', Misproyectos, name='misproyectos'),
    path('agregar-tasador/',  Agregar_usuario, name='agregar_usuario'),
    path('casaz/', Casaz, name='casaz'),
    path('casa_apa/', Casapa, name='casapa'),
    path('casa_arn01/', CasaArn01, name='casaarn01'),
    path('casa_dinamarca/', CasaDina, name='casadinamarca'),
    path('nueva_tasacion/',  Newtasacion, name='newtasacion'),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)