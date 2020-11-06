
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('GradeInquiry.urls')),
    path('teacher/',include('uploadgrade.urls')),

    # path('grades/',include('GradeInquiry.urls'))


]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)