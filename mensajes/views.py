from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Mensaje

class HomeView(View):
    def get(self, request):
        return render(request, 'mensajes/home.html')

class CrearMensajeView(View):
    def get(self, request):
        return render(request, 'mensajes/crear_mensaje.html')

    def post(self, request):
        emisor = request.POST['emisor']
        receptor = request.POST['receptor']
        contenido = request.POST['contenido']
        Mensaje.objects.create(emisor=emisor, receptor=receptor, contenido=contenido)
        return redirect('home')

class VerRecibidosView(View):
    def get(self, request):
        receptor = request.GET.get('receptor')
        mensajes = Mensaje.objects.filter(receptor=receptor)
        return render(request, 'mensajes/mensajes_recibidos.html', {'mensajes': mensajes})

class VerEnviadosView(View):
    def get(self, request):
        emisor = request.GET.get('emisor')
        mensajes = Mensaje.objects.filter(emisor=emisor)
        return render(request, 'mensajes/mensajes_enviados.html', {'mensajes': mensajes})

class EliminarMensajeView(View):
    def get(self, request):
        return render(request, 'mensajes/eliminar_mensaje.html')

    def post(self, request):
        pk = request.POST.get('pk')
        try:
            mensaje = Mensaje.objects.get(pk=pk)
            mensaje.delete()
            return redirect('home')
        except Mensaje.DoesNotExist:
            return render(request, 'mensajes/eliminar_mensaje.html', {'error': 'Mensaje no encontrado'})