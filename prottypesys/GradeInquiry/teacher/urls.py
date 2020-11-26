from django.urls import path

from . import views
from .views import AllGradeShowViewSet

urlpatterns = [
    path('', views.file_upload, name='teacher'),
    path('allgrade/',AllGradeShowViewSet.as_view(),name='allgrade')

]