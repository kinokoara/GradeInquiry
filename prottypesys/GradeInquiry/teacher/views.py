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

class CourseViewSet(generics.ListAPIView):#コースマスタ
    serializer_class = Loginserializers
    queryset = LoginUser.objects.all()

    def list(self,request):
        user = request.user
        queryset = LoginUser.objects.filter(username=user)
        serializer = Loginserializers(queryset,many=True)
        value = serializer.data[0]
        print(value)
        return Response(serializer.data)

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

                    return Response('ok')

                else:
                    return render(request, 'upload_Course.html')

        return file_upload_Course(request)


class DepartViewSet(generics.ListAPIView):#学科マスタ
    serializer_class = Loginserializers
    queryset = LoginUser.objects.all()

    def list(self,request):
        user = request.user
        queryset = LoginUser.objects.filter(username=user)
        serializer = Loginserializers(queryset,many=True)
        value = serializer.data[0]
        print(value)
        return Response(serializer.data)

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

                    return Response('ok')
                else:
                    return render(request, 'upload_Depart.html')

        return file_upload_Depart(request)


class GradeViewSet(generics.ListAPIView):#成績テーブル
    serializer_class = Loginserializers
    queryset = LoginUser.objects.all()

    def list(self,request):
        user = request.user
        queryset = LoginUser.objects.filter(username=user)
        serializer = Loginserializers(queryset,many=True)
        value = serializer.data[0]
        print(value)
        return Response(serializer.data)

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

                    return Response('ok')

                else:
                    return render(request, 'upload_Grade.html')

        return file_upload_Grade(request)



class StudentViewSet(generics.ListAPIView):#学籍マスタ
    serializer_class = Loginserializers
    queryset = LoginUser.objects.all()

    def list(self,request):
        user = request.user
        queryset = LoginUser.objects.filter(username=user)
        serializer = Loginserializers(queryset,many=True)
        value = serializer.data[0]
        print(value)
        return Response(serializer.data)

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

                    return Response('ok')

                else:
                    return render(request, 'upload_Student.html')

        return file_upload_Student(request)


class SubjectViewSet(generics.ListAPIView):#科目テーブル
    serializer_class = Loginserializers
    queryset = LoginUser.objects.all()

    def list(self,request):
        user = request.user
        queryset = LoginUser.objects.filter(username=user)
        serializer = Loginserializers(queryset,many=True)
        value = serializer.data[0]
        print(value)
        return Response(serializer.data)

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
        Astudentarray = ['A0001','A0002','A0003','A0004','A0005','A0006','A0007','A0008','A0009','A0010','A0011','A0012',
                        'A0013','A0014','A0015','A0016','A0017','A0018','A0019','A0020','A0021','A0022','A0023','A0024',
                        'A0025','A0026','A0027','A0028','A0029']

        # 学籍番号 A0,B0,C0,D0の成績表示

        queryset1 = Grade.objects.filter(student_number=Astudentarray[0])
        serializer1 = Gradeserializers(queryset1, many=True,)
        serializer1s = Gradestudentseriarizer(queryset1,many=True,)

        queryset2 = Grade.objects.filter(student_number=Astudentarray[1])
        serializer2 = Gradeserializers(queryset2, many=True, )
        serializer2s = Gradestudentseriarizer(queryset2, many=True, )

        queryset3 = Grade.objects.filter(student_number=Astudentarray[2])
        serializer3 = Gradeserializers(queryset3, many=True, )
        serializer3s = Gradestudentseriarizer(queryset3, many=True, )

        queryset4 = Grade.objects.filter(student_number=Astudentarray[3])
        serializer4 = Gradeserializers(queryset4, many=True, )
        serializer4s = Gradestudentseriarizer(queryset4, many=True, )

        queryset5 = Grade.objects.filter(student_number=Astudentarray[4])
        serializer5 = Gradeserializers(queryset5, many=True, )
        serializer5s = Gradestudentseriarizer(queryset5, many=True, )

        queryset6 = Grade.objects.filter(student_number=Astudentarray[5])
        serializer6 = Gradeserializers(queryset6, many=True, )
        serializer6s = Gradestudentseriarizer(queryset6, many=True, )

        queryset7 = Grade.objects.filter(student_number=Astudentarray[6])
        serializer7 = Gradeserializers(queryset7, many=True, )
        serializer7s = Gradestudentseriarizer(queryset7, many=True, )

        queryset8 = Grade.objects.filter(student_number=Astudentarray[7])
        serializer8 = Gradeserializers(queryset8, many=True, )
        serializer8s = Gradestudentseriarizer(queryset8, many=True, )

        queryset9 = Grade.objects.filter(student_number=Astudentarray[8])
        serializer9 = Gradeserializers(queryset9, many=True, )
        serializer9s = Gradestudentseriarizer(queryset9, many=True, )

        queryset10 = Grade.objects.filter(student_number=Astudentarray[9])
        serializer10 = Gradeserializers(queryset10, many=True, )
        serializer10s = Gradestudentseriarizer(queryset10, many=True, )

        queryset11 = Grade.objects.filter(student_number=Astudentarray[10])
        serializer11 = Gradeserializers(queryset11, many=True, )
        serializer11s = Gradestudentseriarizer(queryset11, many=True, )

        queryset12 = Grade.objects.filter(student_number=Astudentarray[11])
        serializer12 = Gradeserializers(queryset12, many=True, )
        serializer12s = Gradestudentseriarizer(queryset12, many=True, )

        queryset13 = Grade.objects.filter(student_number=Astudentarray[12])
        serializer13 = Gradeserializers(queryset13, many=True, )
        serializer13s = Gradestudentseriarizer(queryset13, many=True, )

        queryset14 = Grade.objects.filter(student_number=Astudentarray[13])
        serializer14 = Gradeserializers(queryset14, many=True, )
        serializer14s = Gradestudentseriarizer(queryset14, many=True, )

        queryset15 = Grade.objects.filter(student_number=Astudentarray[14])
        serializer15 = Gradeserializers(queryset15, many=True, )
        serializer15s = Gradestudentseriarizer(queryset15, many=True, )

        queryset16 = Grade.objects.filter(student_number=Astudentarray[15])
        serializer16 = Gradeserializers(queryset16, many=True, )
        serializer16s = Gradestudentseriarizer(queryset16, many=True, )

        queryset17 = Grade.objects.filter(student_number=Astudentarray[16])
        serializer17 = Gradeserializers(queryset17, many=True, )
        serializer17s = Gradestudentseriarizer(queryset17, many=True, )

        queryset18 = Grade.objects.filter(student_number=Astudentarray[17])
        serializer18 = Gradeserializers(queryset18, many=True, )
        serializer18s = Gradestudentseriarizer(queryset18, many=True, )

        queryset19 = Grade.objects.filter(student_number=Astudentarray[18])
        serializer19 = Gradeserializers(queryset19, many=True, )
        serializer19s = Gradestudentseriarizer(queryset19, many=True, )

        queryset20 = Grade.objects.filter(student_number=Astudentarray[19])
        serializer20 = Gradeserializers(queryset20, many=True, )
        serializer20s = Gradestudentseriarizer(queryset20, many=True, )

        queryset21 = Grade.objects.filter(student_number=Astudentarray[20])
        serializer21 = Gradeserializers(queryset21, many=True, )
        serializer21s = Gradestudentseriarizer(queryset21, many=True, )

        queryset22 = Grade.objects.filter(student_number=Astudentarray[21])
        serializer22 = Gradeserializers(queryset22, many=True, )
        serializer22s = Gradestudentseriarizer(queryset22, many=True, )

        queryset23 = Grade.objects.filter(student_number=Astudentarray[22])
        serializer23 = Gradeserializers(queryset23, many=True, )
        serializer23s = Gradestudentseriarizer(queryset23, many=True, )

        queryset24 = Grade.objects.filter(student_number=Astudentarray[23])
        serializer24 = Gradeserializers(queryset24, many=True, )
        serializer24s = Gradestudentseriarizer(queryset24, many=True, )

        queryset25 = Grade.objects.filter(student_number=Astudentarray[24])
        serializer25 = Gradeserializers(queryset25, many=True, )
        serializer25s = Gradestudentseriarizer(queryset25, many=True, )

        queryset26 = Grade.objects.filter(student_number=Astudentarray[25])
        serializer26 = Gradeserializers(queryset26, many=True, )
        serializer26s = Gradestudentseriarizer(queryset26, many=True, )

        queryset27 = Grade.objects.filter(student_number=Astudentarray[26])
        serializer27 = Gradeserializers(queryset27, many=True, )
        serializer27s = Gradestudentseriarizer(queryset27, many=True, )

        queryset28 = Grade.objects.filter(student_number=Astudentarray[27])
        serializer28 = Gradeserializers(queryset28, many=True, )
        serializer28s = Gradestudentseriarizer(queryset28, many=True, )

        queryset29 = Grade.objects.filter(student_number=Astudentarray[28])
        serializer29 = Gradeserializers(queryset29, many=True, )
        serializer29s = Gradestudentseriarizer(queryset29, many=True, )

        return Response(
            [# A
                [# A0
                    [ #学籍番号の判定
                        [serializer1s.data[0],serializer1.data],
                        [serializer2s.data[0],serializer2.data],
                        [serializer3s.data[0], serializer3.data],
                        [serializer4s.data[0], serializer4.data],
                        [serializer5s.data[0],serializer5.data],
                        [serializer6s.data[0],serializer6.data],
                        [serializer7s.data[0],serializer7.data],
                        [serializer8s.data[0],serializer8.data],
                        [serializer9s.data[0],serializer9.data],
                        [serializer10s.data[0],serializer10.data],
                        [serializer11s.data[0],serializer11.data],
                        [serializer12s.data[0],serializer12.data],
                        [serializer13s.data[0],serializer13.data],
                        [serializer14s.data[0],serializer14.data],
                        [serializer15s.data[0],serializer15.data],
                        [serializer16s.data[0],serializer16.data],
                        [serializer17s.data[0], serializer17.data],
                        [serializer18s.data[0], serializer18.data],
                        [serializer19s.data[0], serializer19.data],
                        [serializer20s.data[0], serializer20.data],
                        [serializer21s.data[0], serializer21.data],
                        [serializer22s.data[0], serializer22.data],
                        [serializer23s.data[0], serializer23.data],
                        [serializer24s.data[0], serializer24.data],
                        [serializer25s.data[0], serializer25.data],
                        [serializer26s.data[0], serializer26.data],
                        [serializer27s.data[0], serializer27.data],
                        [serializer28s.data[0], serializer28.data],
                        [serializer29s.data[0], serializer29.data],
                        ],
                ],
            ],

            [ #B
                [#B0
                    [#学籍番号の判定

                    ]

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





