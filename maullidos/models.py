from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # Aquí puedes agregar campos adicionales en el futuro si lo necesitas
    pass

class Maullido(models.Model):
    contenido = models.CharField(max_length=140)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='maullidos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.contenido[:50]
