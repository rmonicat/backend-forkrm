from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from .serializers import LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class LoginView(APIView):
    @extend_schema(request=LoginSerializer, responses=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            usuario = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=usuario, password=password)

            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return render(request, 'login.html', {'text': "Por favor ingrese su usuario"})


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
