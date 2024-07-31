from django.urls import path
from . import views

urlpatterns = [path('buscar/', views.buscar_libros, name='buscar_libros'),]

from django.contrib import admin
from django.urls import include, path 

urlpatterns = [path('admin/', admin.site.urls),path('mi_aplicacion/',include('mi_aplicacion.urls'))]
