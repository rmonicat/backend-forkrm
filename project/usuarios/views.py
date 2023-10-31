from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def login_users(request, mensaje=""):
    if request.method != "POST":
        return render(request, 'authenticate/login.html', {'text': mensaje})

    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is None:
        messages.success(
            request, 'Hubo un error, por favor intente nuevamente')
        return render(request, 'authenticate/login.html', {'mensaje': 'Hubo un error, por favor intente nuevamente'})

#        return redirect('login', 'Hubo un error, por favor intente nuevamente')

    login(request, user)
    return redirect('asyncTest')
