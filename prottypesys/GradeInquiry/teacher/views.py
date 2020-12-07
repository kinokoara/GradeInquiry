import re

from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from GradeInquiry.models import Grade, Subject, Course, Depart, Student,LoginUser
from io import TextIOWrapper

import csv


# ------------------------------------------------------------------
from GradeInquiry.serializers import Gradeserializers,Loginserializers,Gradestudentseriarizer

class CourseViewSet(generics.ListCreateAPIView):#コースマスタ
    serializer_class = Loginserializers
    queryset = LoginUser.objects.all()

    def post(self,request):
        user = str(request.user)
        pattern = '^B.?[0-9]{4}'
        result1 = re.fullmatch(pattern, user)
        if result1:
            return 'error'

        else:

            def file_upload_Course(request):
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

        return file_upload_Course(request)


class DepartViewSet(generics.ListAPIView):#学科マスタ
    serializer_class = Loginserializers
    queryset = LoginUser.objects.all()

    def post(self,request):
        user = str(request.user)
        pattern = '^B.?[0-9]{4}'
        result1 = re.fullmatch(pattern, user)
        if result1:
            return 'error'

        else:

            def file_upload_Depart(request):
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

        return file_upload_Depart(request)


class GradeViewSet(generics.ListAPIView):#成績テーブル
    serializer_class = Loginserializers
    queryset = LoginUser.objects.all()

    def post(self,request):
        user = str(request.user)
        pattern = '^B.?[0-9]{4}'
        result1 = re.fullmatch(pattern, user)
        if result1:
            return 'error'

        else:

            def file_upload_Grade(request):
                if 'csv' in request.FILES:
                    csv_file = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
                    csv_import = csv.reader(csv_file)
                    header = next(csv_import)
                    for line in csv_import:
                        grade, created = Grade.objects.get_or_create(
                            grade_id=line[0])

                        grade.evaluation = line[1]
                        grade.subject_id = Subject.objects.get(subject_id=line[2])
                        grade.student_number = line[3]
                        grade.save()

                    return render(request, 'upload_Grade.html')

                else:
                    return render(request, 'upload_Grade.html')

        return file_upload_Grade(request)



class StudentViewSet(generics.ListAPIView):#学籍マスタ
    serializer_class = Loginserializers
    queryset = LoginUser.objects.all()

    def post(self,request):
        user = str(request.user)
        pattern = '^B.?[0-9]{4}'
        result1 = re.fullmatch(pattern, user)
        if result1:
            return 'error'

        else:

            def file_upload_Student(request):
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

        return file_upload_Student(request)


class SubjectViewSet(generics.ListAPIView):#科目テーブル
    serializer_class = Loginserializers
    queryset = LoginUser.objects.all()

    def post(self,request):
        user = str(request.user)
        pattern = '^B.?[0-9]{4}'
        result1 = re.fullmatch(pattern, user)
        if result1:
            return 'error'

        else:

            def file_upload_Subject(request):
                if 'csv' in request.FILES:
                    csv_file = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
                    csv_import = csv.reader(csv_file)
                    header = next(csv_import)
                    for line in csv_import:
                        subject, created = Subject.objects.get_or_create(
                            subject_id=line[0])

                        subject.subject_name = line[1]
                        subject.units = line[2]
                        subject.dividend_period = line[3]
                        subject.save()

                    return render(request, 'upload_Subject.html')

                else:
                    return render(request, 'upload_Subject.html')

        return file_upload_Subject(request)


class SourtGradeShowViewSet(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = Gradeserializers
    '''
    成績取得のgetメソッドのrequestがきた時の処理の記述
    '''

    def list(self, request):
        user = request.user
        # queryset = Grade.objects.all()
        # serializer = Gradeserializers(queryset,many=True)


        # 学籍番号 A0,B0,C0,D0の成績表示

        queryset1 = Grade.objects.filter(student_number__iregex=r'^A0001$')
        serializer1 = Gradeserializers(queryset1, many=True,)
        serializer1s = Gradestudentseriarizer(queryset1,many=True,)


        querysetb = Grade.objects.filter(student_number__iregex=r'^A0002$')
        serializerb = Gradeserializers(querysetb, many=True,)
        serializerbs = Gradestudentseriarizer(querysetb,many=True,)




        return Response(
            [# A
                [# A0
                        [ #学籍番号の判定
                            [serializer1s.data[0],serializer1.data], #A0001の学籍番号と成績
                            [serializerbs.data[0],serializerb.data], #A0002の学籍番号と成績
                        ],
                ],
            ])
class AllGradeShowViewSet(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = Gradeserializers
    '''
    成績取得のgetメソッドのrequestがきた時の処理の記述
    '''

    def list(self, request):
        user = request.user
        queryset = Grade.objects.filter(grade_id__gte=1)
        serializer = Gradeserializers(queryset,many=True)
        return Response(serializer.data)





