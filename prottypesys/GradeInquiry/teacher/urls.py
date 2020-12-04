from django.urls import path
from . import views
from .views import AllGradeShowViewSet, CourseViewSet, DepartViewSet, GradeViewSet, StudentViewSet, SubjectViewSet


urlpatterns = [
    # path('', views.file_upload, name='teacher'),
<<<<<<< HEAD
    path('Course/', CourseViewSet.as_view(), name='Course'),
    path('Depart/', DepartViewSet.as_view(), name='Depart'),
    path('Grade/', GradeViewSet.as_view(), name='Grade'),
    path('Student/', StudentViewSet.as_view(), name='Student'),
    path('Subject/', SubjectViewSet.as_view(), name='Subject'),
    path('allgrade/',AllGradeShowViewSet.as_view(),name='allgrade')


=======
    path('Course/', views.file_upload_Course, name='Course'),
    path('Depart/', views.file_upload_Depart, name='Depart'),
    path('Grade/', views.file_upload_Grade, name='Grade'),
    path('Student/', views.file_upload_Student, name='Student'),
    path('Subject/', views.file_upload_Subject, name='Subject'),
    path('allgrade/',AllGradeShowViewSet.as_view(),name='allgrade'),
    # path('agrade/',AGradeShowViewSet.as_view(),name='agrade'),
    # path('bgrade/', BGradeShowViewSet.as_view(), name='bgrade'),
    # path('cgrade/', CGradeShowViewSet.as_view(), name='cgrade'),
    # path('dgrade/', DGradeShowViewSet.as_view(), name='dgrade'),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 1e9525dee2938db7045f6b7d70cd9ff5e1e8e5f6
=======
>>>>>>> 1e9525dee2938db7045f6b7d70cd9ff5e1e8e5f6
=======
>>>>>>> 1e9525dee2938db7045f6b7d70cd9ff5e1e8e5f6
=======
>>>>>>> 1e9525dee2938db7045f6b7d70cd9ff5e1e8e5f6
=======
>>>>>>> 1e9525dee2938db7045f6b7d70cd9ff5e1e8e5f6
]