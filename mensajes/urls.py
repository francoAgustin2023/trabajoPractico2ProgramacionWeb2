from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('crear/', views.CrearMensajeView.as_view(), name='crear_mensaje'),
    path('recibidos/', views.VerRecibidosView.as_view(), name='mensajes_recibidos'),
    path('enviados/', views.VerEnviadosView.as_view(), name='mensajes_enviados'),
    path('eliminar/', views.EliminarMensajeView.as_view(), name='eliminar_mensaje'),
]
