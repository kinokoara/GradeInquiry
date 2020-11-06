from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from django.contrib.auth.views import LoginView
from django.views import generic
from django.views.generic import View
from .models import Student

from .models import LoginUser
from .serializers  import Userserializers


class CreateUserView(generics.CreateAPIView):
    serializer_class = Userserializers
    permission_classes = (AllowAny,)




