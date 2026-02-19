from django.db import models
from zonas.models import Zona

class Autobus(models.Model):
    nombre = models.CharField(max_length=100)
    origen = models.CharField(max_length=150)
    destino = models.CharField(max_length=150)
    zona = models.ForeignKey(
        Zona,
        on_delete=models.CASCADE,
        related_name="autobuses"
    )

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Autobús"
        verbose_name_plural = "Autobuses"
