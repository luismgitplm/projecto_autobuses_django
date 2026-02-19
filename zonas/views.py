from django.views.generic import ListView
from .models import Zona

class ListadoZonasView(ListView):
    model = Zona
    template_name = "zonas/listado_zonas.html"
