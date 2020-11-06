

from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from GradeInquiry.models import Student


def Upload(request):
    student_data  = Student.objects.all()

    return render(request,'teacher.html',{'student_data':student_data})