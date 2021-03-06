from django.contrib import admin
from rest_framework import routers
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import CreateUserView,LoginView,AddPostcontentView,DeletepostView,SecretView,ChangePasswordView
from . import views



urlpatterns = [

    path('create/',CreateUserView.as_view(),name='create'),
    # path('teacher/',UploadView.as_view(),name='upload'),
    path('student/',include('GradeInquiry.Student.urls')),
    path('teacher/',include('GradeInquiry.teacher.urls')),
    path('authenticate/', include('djoser.urls.jwt')),
    path('login/',LoginView.as_view(),name='login'),
    path('contents/',AddPostcontentView.as_view(),name='post'),
    path('contents/<int:pk>/',DeletepostView.as_view(),name='delete'),
    path('keyinquey/',SecretView.as_view(),name='secret'),
    path('changepw/<int:pk>', ChangePasswordView.as_view(),name='changePW')



]