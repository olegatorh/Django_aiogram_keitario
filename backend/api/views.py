from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import User
from .serializers import UsersSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
