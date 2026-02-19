from django.views.generic import ListView
from .models import Autobus

class ListadoAutobusesView(ListView):
    model = Autobus
    template_name = "autobuses/listado_autobuses.html"
