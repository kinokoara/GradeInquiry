from django.urls import path
from .import views
from .views import SourtGradeShowViewSet, CourseViewSet, DepartViewSet, GradeViewSet, StudentViewSet, SubjectViewSet,ChangefileStyleViewSet


urlpatterns = [
    # path('', views.file_upload, name='teacher'),
    path('Course/', CourseViewSet.as_view(), name='Course'),
    path('Depart/', DepartViewSet.as_view(), name='Depart'),
    path('Grade/', GradeViewSet.as_view(), name='Grade'),
    path('Student/', StudentViewSet.as_view(), name='Student'),
    path('Subject/', SubjectViewSet.as_view(), name='Subject'),
    path('sourtgrade/',SourtGradeShowViewSet.as_view(),name='sourtgrade'),
    # path('allgrade/',AllGradeShowViewSet.as_view(),name='allgrade')
    path('change/',ChangefileStyleViewSet.as_view(),name='changestyle')
]