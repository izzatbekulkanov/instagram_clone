from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import SignUpSerializer
from .models import User

# Create your views here.

class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions, AllowAny)
    serializer_class = SignUpSerializer

