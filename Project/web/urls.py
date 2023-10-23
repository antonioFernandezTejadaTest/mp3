from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, convertidor_youtube

urlpatterns = {
    path('info', views.info, name='obtener_info'),
    path('descargar', views.descargar_audio, name="descargar"),
    path('descargar/archivo', views.descargar_archivo, name="descargar_archivo"),
    path('', views.home),
}