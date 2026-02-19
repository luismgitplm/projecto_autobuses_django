from django.urls import path
from .views import ListadoZonasView

urlpatterns = [
    path('zonas/', ListadoZonasView.as_view(), name='listado_zonas'),
]
