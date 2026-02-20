from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Eleccion
from autobuses.models import Autobus

class MisEleccionesListView(LoginRequiredMixin, ListView):
    model = Eleccion
    template_name = "elecciones/mis_elecciones.html"

    def get_queryset(self):
        return Eleccion.objects.filter(usuario=self.request.user)


class CrearEleccionView(LoginRequiredMixin, CreateView):
    model = Eleccion
    fields = ['autobus']
    template_name = "elecciones/eleccion_form.html"
    success_url = "/mis-elecciones/"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class BorrarEleccionView(LoginRequiredMixin, DeleteView):
    model = Eleccion
    template_name = "elecciones/eleccion_confirm_delete.html"
    success_url = "/mis-elecciones/"

    def get_queryset(self):
        return Eleccion.objects.filter(usuario=self.request.user)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('mis_elecciones') 
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
