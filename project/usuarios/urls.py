from django.contrib import admin
from django.urls import path, include
from usuarios.views import login_users


urlpatterns = [
    path('login_user/', login_users, name='login'),
    path('login_user/<str:mensaje>/', login_users, name='loginConMensaje'),
]
a = 9
