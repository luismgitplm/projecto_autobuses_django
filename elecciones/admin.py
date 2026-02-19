from django.contrib import admin
from .models import Eleccion

@admin.register(Eleccion)
class EleccionAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'autobus', 'fecha_creacion')
    list_filter = ('usuario', 'autobus')
    search_fields = ('usuario__username', 'autobus__nombre')
