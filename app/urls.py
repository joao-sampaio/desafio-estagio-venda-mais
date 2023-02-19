from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.cadastro),
    path('', views.login),
    path('login', views.login),
]