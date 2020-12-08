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
        # Astudentarray = ['A0001','A0002','A0003','A0004','A0005','A0006','A0007','A0008','A0009','A0010','A0011','A0012',
        #                 'A0013','A0014','A0015','A0016','A0017','A0018','A0019','A0020','A0021','A0022','A0023','A0024',
        #                 'A0025','A0026','A0027','A0028','A0029']




        querysets = Grade.objects.filter(student_number__iregex='^[A-D].*$')
        serialisers = Gradestudentseriarizer(querysets, many=True, )
        serialisersarray = (list(serialisers.data[0].values()))


        for i in range(1,100):
            student_num = (list(serialisers.data[i].values()))
            serialisersarray.append(student_num[0])

            studentarray = (list(serialisers.data))

        queryset = []
        serialiser = []
        for i in range(100):
            queryset.append(Grade.objects.filter(student_number=serialisersarray[i]))
            serialiser.append(Gradeserializers(queryset[i], many=True,))

        Alist = []
        Blist = []
        Clist = []
        Dlist = []
        # Alist =  [[[[studentarray[0], serialiser[0].data]]]]



        for i in range(0, 29):
            Alist.append([studentarray[i], serialiser[i].data])
        for i in range(30,60):
            Blist.append([studentarray[i], serialiser[i].data])
        for i in range(61,87):
            Clist.append([studentarray[i], serialiser[i].data])
        for i in range(88,99):
            Dlist.append([studentarray[i], serialiser[i].data])


        return Response(
        [
            [
                    Alist
            ],
            [

                    Blist

            ],
            [

                    Clist

            ],
            [

                    Dlist

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





