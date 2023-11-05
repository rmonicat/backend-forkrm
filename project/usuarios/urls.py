from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path('login/', views.LoginView.as_view(), name='login'),
    #   path('login/', views.LoginView.as_view(), name='loginClass'),
    path('login_user/', views.login_users, name='loginxx'),
    path('login_user/<str:mensaje>/', views.login_users, name='loginConMensaje'),
]
a = 9
