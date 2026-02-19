from django.urls import path
from .views import MisEleccionesListView, CrearEleccionView, BorrarEleccionView
from . import views

urlpatterns = [
    path('mis-elecciones/', MisEleccionesListView.as_view(), name='mis_elecciones'),
    path('crear-eleccion/', CrearEleccionView.as_view(), name='crear_eleccion'),
    path('borrar-eleccion/<int:pk>/', BorrarEleccionView.as_view(), name='borrar_eleccion'),
    path('signup/', views.signup, name='signup'),
]
