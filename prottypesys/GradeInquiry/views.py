from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.viewsets import ViewSet
from django.contrib.auth.views import LoginView
from django.views import generic
from django.views.generic import View, ListView
from .models import Student,Grade

from .models import LoginUser
from .serializers  import Userserializers,Gradeserializers


class CreateUserView(generics.CreateAPIView):
    serializer_class = Userserializers
    permission_classes = (AllowAny,)


class GradeShowViewSet(viewsets.ModelViewSet):
    serializer_class = Gradeserializers
    queryset = Grade.objects.all()
    # permission_classes = (IsAuthenticated)




