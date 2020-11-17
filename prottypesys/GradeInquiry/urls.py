from django.contrib import admin
from rest_framework import routers
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import CreateUserView,GradeShowViewSet,LoginView,AllGradeShowViewSet
from . import views



urlpatterns = [

    path('create/',CreateUserView.as_view(),name='create'),
    # path('teacher/',UploadView.as_view(),name='upload'),
    path('indivgrade/',GradeShowViewSet.as_view()),
    path('authenticate/', include('djoser.urls.jwt')),
    path('login/',LoginView.as_view(),name='login'),
    path('allgrade/',AllGradeShowViewSet.as_view())

]