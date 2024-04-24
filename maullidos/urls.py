#urls.py de maullidos
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import IndexView, MaullidoCreateView, UserMaullidosView, RegistroView, readme_view, CustomLogoutView, ContactView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('maullido/create/', MaullidoCreateView.as_view(), name='maullido-create'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('usuarios/<str:username>/', UserMaullidosView.as_view(), name='user-maullidos'),
    path('README.md', readme_view, name='readme'),
    path('contacto/', ContactView.as_view(), name='contacto'),
]
