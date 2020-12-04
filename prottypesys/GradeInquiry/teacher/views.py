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
from GradeInquiry.serializers import Gradeserializers,Loginserializers

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
        queryseta = Grade.objects.filter(student_number__iregex=r'^A0.*$')
        serializera = Gradeserializers(queryseta, many=True,)
        querysetb = Grade.objects.filter(student_number__iregex=r'^B0.*$')
        serializerb = Gradeserializers(querysetb, many=True,)
        querysetc = Grade.objects.filter(student_number__iregex=r'^C0.*$')
        serializerc = Gradeserializers(querysetc, many=True, )
        querysetd = Grade.objects.filter(student_number__iregex=r'^D0.*$')
        serializerd = Gradeserializers(querysetd, many=True, )


        # 学籍番号 A1,B1,C1,D1の成績表示
        querysetao = Grade.objects.filter(student_number__iregex=r'^A1.*$')
        serializerao = Gradeserializers(querysetao, many=True, )
        querysetbo = Grade.objects.filter(student_number__iregex=r'^B1.*$')
        serializerbo = Gradeserializers(querysetbo, many=True, )
        querysetco = Grade.objects.filter(student_number__iregex=r'^C1.*$')
        serializerco = Gradeserializers(querysetco, many=True, )
        querysetdo = Grade.objects.filter(student_number__iregex=r'^D1.*$')
        serializerdo = Gradeserializers(querysetdo, many=True, )

        # 学籍番号 A2,B2,C2,D2の成績表示
        querysetat = Grade.objects.filter(student_number__iregex=r'^A2.*$')
        serializerat = Gradeserializers(querysetat, many=True, )
        querysetbt = Grade.objects.filter(student_number__iregex=r'^B2.*$')
        serializerbt = Gradeserializers(querysetbt, many=True, )
        querysetct = Grade.objects.filter(student_number__iregex=r'^C2.*$')
        serializerct = Gradeserializers(querysetct, many=True, )
        querysetdt = Grade.objects.filter(student_number__iregex=r'^D2.*$')
        serializerdt = Gradeserializers(querysetdt, many=True, )



        return Response([
            [
            serializera.data,
            serializerao.data,
            serializerat.data,
            ],
            [
            serializerb.data,
            serializerbo.data,
            serializerbt.data,
            ],
            [
            serializerc.data,
            serializerco.data,
            serializerct.data,
            ],
            [
            serializerd.data,
            serializerdo.data,
            serializerdt.data
            ]
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





