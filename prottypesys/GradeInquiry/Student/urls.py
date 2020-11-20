from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import GradeShowViewSet
urlpatterns = [
    path('indivgrade',GradeShowViewSet.as_view(),name='indiv')
]