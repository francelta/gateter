# Description: Este archivo contiene las vistas de la aplicación maullidos.
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login
from .forms import RegistroForm
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Maullido, Usuario
from .forms import MaullidoForm
from django.contrib.auth import logout as auth_logout
from django.views import View
from django.http import HttpResponse
import os
from django.conf import settings

def readme_view(request):
    # Construye la ruta absoluta al archivo README.md
    file_path = os.path.join(settings.BASE_DIR, 'static', 'README.md')

    # Intenta abrir y leer el archivo
    try:
        with open(file_path, 'r',encoding='utf-8') as file:
            content = file.read()
            return HttpResponse(content, content_type='text/plain')
    except FileNotFoundError:
        return HttpResponse(f"El archivo README.md no se encontró. {file_path}", status=404)

class RegistroView(generic.CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registro.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

class MaullidoCreateView(LoginRequiredMixin, CreateView):
    model = Maullido
    form_class = MaullidoForm
    template_name = 'maullidos/maullido_form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_extra_nav'] = True  
        return context
    

class UserMaullidosView(ListView):
    model = Maullido
    template_name = 'maullidos/user_maullidos.html'
    context_object_name = 'maullidos'
    paginate_by = 10
     

    def get_queryset(self):
        self.usuario = get_object_or_404(Usuario, username=self.kwargs['username'])
        return Maullido.objects.filter(usuario=self.usuario).order_by('-fecha_creacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_user'] = self.usuario  
        context['usuarios_lista'] = Usuario.objects.all() 
        return context


class IndexView(TemplateView):
    template_name = 'maullidos/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuarios_lista'] = Usuario.objects.all()  
        if self.request.user.is_authenticated:
            context['maullidos'] = Maullido.objects.filter(usuario=self.request.user).order_by('-fecha_creacion')
        return context


class CustomLogoutView(View):
    def get(self, request):
        auth_logout(request)
        return redirect('/')  

class ContactView(TemplateView):
    template_name = 'maullidos/contacto.html'

    

