from django.urls import path

from . import views
from .views import AllGradeShowViewSet

urlpatterns = [
    # path('', views.file_upload, name='teacher'),
    path('Course/', views.file_upload_Course, name='Course'),
    path('Depart/', views.file_upload_Depart, name='Depart'),
    path('Grade/', views.file_upload_Grade, name='Grade'),
    path('Student/', views.file_upload_Student, name='Student'),
    path('Subject/', views.file_upload_Subject, name='Subject'),
    path('allgrade/',AllGradeShowViewSet.as_view(),name='allgrade')

]