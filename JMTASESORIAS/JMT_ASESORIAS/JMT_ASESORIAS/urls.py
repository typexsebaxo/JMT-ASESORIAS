"""JMT_ASESORIAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings

urlpatterns = [
    path('inicioSesion/',views.InicioSesion, name='InicioSesion'),
    path('menuadmin/',views.Menuadmin, name='menuadmin'),
    path('admintasador/',views.Admintasador, name='admintasador'),
    path('menutasacionadmin/',views.Menutasacionadmin, name='menutasacionadmin'),
    path('graficostasacion/',views.Graficostasacion, name='graficostasacion'),
    path('notificacionesadmin/',views.Notificacionesadmin, name='notificacionesadmin'),
    path('creatasador/',views.Creatasador, name='creatasador'),
    path('menutasador/',views.Menutasador, name='menutasador'),
    path('misproyectos/',views.Misproyectos, name='misproyectos'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)