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

        # 学籍番号 A3,B3,C3,D3の成績表示
        # querysetatt = Grade.objects.filter(student_number__iregex=r'^A3.*$')
        # serializeratt = Gradeserializers(querysetatt, many=True, )
        # querysetbtt = Grade.objects.filter(student_number__iregex=r'^B3.*$')
        # serializerbtt = Gradeserializers(querysetbtt, many=True, )
        # querysetctt = Grade.objects.filter(student_number__iregex=r'^C3.*$')
        # serializerctt = Gradeserializers(querysetctt, many=True, )
        # querysetdtt = Grade.objects.filter(student_number__iregex=r'^D3.*$')
        # serializerdtt = Gradeserializers(querysetdtt, many=True, )


        # 学籍番号 A4,B4,C4,D4の成績表示
        # querysetaf = Grade.objects.filter(student_number__iregex=r'^A4.*$')
        # serializeraf = Gradeserializers(querysetaf, many=True, )
        # querysetbf = Grade.objects.filter(student_number__iregex=r'^B4.*$')
        # serializerbf = Gradeserializers(querysetbf, many=True, )
        # querysetcf = Grade.objects.filter(student_number__iregex=r'^C4.*$')
        # serializercf = Gradeserializers(querysetcf, many=True, )
        # querysetdf = Grade.objects.filter(student_number__iregex=r'^D4.*$')
        # serializerdf = Gradeserializers(querysetdf, many=True, )



        return Response({
            'GradeA0':serializera.data,
            'GradeB0':serializerb.data,
            'GradeC0':serializerc.data,
            'GradeD0':serializerd.data,

            'GradeA1': serializerao.data,
            'GradeB1': serializerbo.data,
            'GradeC1': serializerco.data,
            'GradeD1': serializerdo.data,

            'GradeA2': serializerat.data,
            'GradeB2': serializerbt.data,
            'GradeC2': serializerct.data,
            'GradeD2': serializerdt.data,

            # 'GradeA3': serializeratt.data,
            # 'GradeB3': serializerbtt.data,
            # 'GradeC3': serializerctt.data,
            # 'GradeD3': serializerdtt.data,
            #
            # 'GradeA4': serializeraf.data,
            # 'GradeB4': serializerbf.data,
            # 'GradeC4': serializercf.data,
            # 'GradeD4': serializerdf.data,

        })


# 学籍番号Aから始まる人
# class AGradeShowViewSet(generics.ListCreateAPIView):
#     queryset = Grade.objects.all()
#     serializer_class = Gradeserializers
#
#     def list(self, request):
#         user = request.user
#         queryset = Grade.objects.filter(student_number__iregex=r'^A.*$')
#         serializer = Gradeserializers(queryset, many=True, )
#         return Response(serializer.data)
#
#
# # 学籍番号Bから始まる人
# class BGradeShowViewSet(generics.ListCreateAPIView):
#     queryset = Grade.objects.all()
#     serializer_class = Gradeserializers
#
#     def list(self, request):
#         user = request.user
#         queryset = Grade.objects.filter(student_number__iregex=r'^B.*$')
#         serializer = Gradeserializers(queryset, many=True, )
#         return Response(serializer.data)
#
#
# # 学籍番号Cから始まる人
# class CGradeShowViewSet(generics.ListCreateAPIView):
#     queryset = Grade.objects.all()
#     serializer_class = Gradeserializers
#
#     def list(self, request):
#         user = request.user
#         queryset = Grade.objects.filter(student_number__iregex=r'^C.*$')
#         serializer = Gradeserializers(queryset, many=True, )
#         return Response(serializer.data)
#
#
# # 学籍番号Dから始まる人
# class DGradeShowViewSet(generics.ListCreateAPIView):
#     queryset = Grade.objects.all()
#     serializer_class = Gradeserializers
#
#     def list(self, request):
#         user = request.user
#         queryset = Grade.objects.filter(student_number__iregex=r'^D.*$')
#         serializer = Gradeserializers(queryset, many=True, )
#         return Response(serializer.data)


