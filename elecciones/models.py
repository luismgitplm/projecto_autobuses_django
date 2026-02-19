from django.db import models
from django.contrib.auth import get_user_model
from autobuses.models import Autobus

User = get_user_model()

class Eleccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    autobus = models.ForeignKey(Autobus, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['usuario', 'autobus'],
                name='unique_usuario_autobus'
            )
        ]
        verbose_name = "Elección"
        verbose_name_plural = "Elecciones"

    def __str__(self):
        return f"{self.usuario.username} - {self.autobus.nombre}"
