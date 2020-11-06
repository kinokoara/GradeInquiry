from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import Upload

urlpatterns = [
    path('upload/',views.Upload,name='upload')
    # path('grades/',include('GradeInquiry.urls'))


]