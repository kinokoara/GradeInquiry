from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
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

# ユーザーの成績表示
class GradeShowViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView,):

    username = 'b91100'

    if (len(username) ==5):
        queryset = Grade.objects.filter(student_number=username)
        serializer_class = Gradeserializers
        permission_classes = (AllowAny,)
        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)
        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)
    elif(len(username) >= 5):
        queryset = Grade.objects.all()
        serializer_class = Gradeserializers
        permission_classes = (AllowAny,)
        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)
        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)




