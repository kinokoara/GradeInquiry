from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response

from GradeInquiry.models import Grade, Subject, Course, Depart, Student
from io import TextIOWrapper

import csv


# ------------------------------------------------------------------
from GradeInquiry.serializers import Gradeserializers

def file_upload_Course(request):#コースマスタ
    if 'csv' in request.FILES:
        csv_file = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_import = csv.reader(csv_file)
        header = next(csv_import)
        for line in csv_import:
            course, created = Course.objects.get_or_create(
                course_id=line[0])

            course.course_name = line[1]
            course.depart_id = line[2]
            course.save()

        return render(request, 'upload_Course.html')

    else:
        return render(request, 'upload_Course.html')

def file_upload_Depart(request):#学科マスタ
    if 'csv' in request.FILES:
        csv_file = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_import = csv.reader(csv_file)
        header = next(csv_import)
        for line in csv_import:
            depart, created = Depart.objects.get_or_create(
                depart_id=line[0])

            depart.depart_name = line[1]
            depart.save()

        return render(request, 'upload_Depart.html')

    else:
        return render(request, 'upload_Depart.html')

def file_upload_Grade(request):#成績テーブル
    if 'csv' in request.FILES:
        csv_file = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_import = csv.reader(csv_file)
        header = next(csv_import)
        for line in csv_import:
            grade, created = Grade.objects.get_or_create(
                grade_id=line[0])

            grade.subject_id = line[1]
            grade.student_number = line[2]
            grade.evaluation = line[3]
            grade.save()

        return render(request, 'upload_Grade.html')

    else:
        return render(request, 'upload_Grade.html')

def file_upload_Student(request):#学籍マスタ
    if 'csv' in request.FILES:
        csv_file = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_import = csv.reader(csv_file)
        header = next(csv_import)
        for line in csv_import:
            student, created = Student.objects.get_or_create(
                student_number=line[0])

            student.student_name = line[1]
            student.class_number = line[2]
            student.couse_id = line[3]
            student.enrolled_id = line[4]

            # student.birthday =[]
            student.save()

        return render(request, 'upload_Student.html')

    else:
        return render(request, 'upload_Student.html')

def file_upload_Subject(request):#科目テーブル
    if 'csv' in request.FILES:
        csv_file = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_import = csv.reader(csv_file)
        header = next(csv_import)
        for line in csv_import:
            subject, created = Subject.objects.get_or_create(
                subject_id=line[0])

            subject.subject_name = line[1]
            subject.dividend_period = line[2]
            subject.units = line[3]
            subject.save()

        return render(request, 'upload_Subject.html')

    else:
        return render(request, 'upload_Subject.html')




class AllGradeShowViewSet(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = Gradeserializers
    '''
    成績取得のgetメソッドのrequestがきた時の処理の記述
    '''

    def list(self, request):
        user = request.user
        # pattern = '^b9.?[0-9]{3}'
        queryset = Grade.objects.filter(student_number__iregex=r'^b9.*$')
        serializer = Gradeserializers(queryset, many=True,)
        return Response(serializer.data)


