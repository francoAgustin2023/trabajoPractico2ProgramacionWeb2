from django.db import models

class Mensaje(models.Model):
    EMISORES_POSIBLES = [
        ('juan', 'Juan'),
        ('maria', 'Maria'),
    ]

    emisor = models.CharField(max_length=5, choices=EMISORES_POSIBLES)
    receptor = models.CharField(max_length=5, choices=EMISORES_POSIBLES)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.emisor} a {self.receptor}: {self.contenido}'