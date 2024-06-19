from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about/',views.about,name='about'),
    path('galeria/',views.galeria,name='galeria'),
    path('formulario/',views.formulario,name='formulario'),
    path('noticias/',views.noticias,name='noticias'),
    path('api/',views.api,name='api'),
]
