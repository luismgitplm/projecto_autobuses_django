from django.urls import path
from .views import ListadoAutobusesView

urlpatterns = [
    path('autobuses/', ListadoAutobusesView.as_view(), name='listado_autobuses'),
]
