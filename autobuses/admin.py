from django.contrib import admin
from .models import Autobus

@admin.register(Autobus)
class AutobusAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'origen', 'destino', 'zona')
    list_filter = ('zona',)
    search_fields = ('nombre', 'origen', 'destino')
