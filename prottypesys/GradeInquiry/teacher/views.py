import re
import shutil
import zipfile

import pandas
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from rest_framework import generics
from rest_framework.response import Response
from GradeInquiry.models import Grade, Subject, Course, Depart, Student, LoginUser, Sheet
from io import TextIOWrapper
MEDIA_ROOT = 'exelfiles/'
ZIP_ROOT = 'GradeInquiry/teacher/zip.zip'
import csv
from GradeInquiry.serializers import Gradeserializers, Loginserializers, Gradestudentseriarizer, Unitserializer,Sheetserialiser


class CourseViewSet(generics.ListAPIView): #コースマスタ
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
                        subject.lecture_name = line[4]
                        subject.save()

                    return Response('ok')

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
        global allunit
        user = request.user
        gradeint_array = []
        unit_array = []
        grade_content = ['秀', '優', '良', '可', '不可']
        grate_array = []
        unitall_array = []
        iflen = 0

        '''
        学生の学籍番号を全て取得してきている
        serialisersarrayは学籍番号のみを全て取得
        studentarrayは学籍番号と項目名を一緒に取得している
        '''
        querysets = Grade.objects.filter(student_number__iregex='^[A-D].*$')
        serialisers = Gradestudentseriarizer(querysets, many=True, )
        serialisersarray = (list(serialisers.data[0].values()))


        for i in range(1,100):
            student_num = (list(serialisers.data[i].values()))
            serialisersarray.append(student_num[0])
            studentarray = (list(serialisers.data))

        print(serialisersarray)
        userlen = len(serialisersarray)

        '''
                各学生ごとの評定平均処理
                '''
        for n in range(userlen):

            unit_all = 0
            gradeint_array = []
            unitall_array = []
            unit_array = []
            sum_array = []
            numgrade_dict = {}

            queryset = Grade.objects.filter(student_number=serialisersarray[n])
            data_int = len(queryset)
            print('データの数',data_int)
            serializer = Gradeserializers(queryset, many=True)
            unit_serializer = Unitserializer(queryset, many=True)
            print(unit_serializer)

            for x in range(data_int):

                unit_num = (list(unit_serializer.data[x].values()))
                outarray = unit_num[0]
                unit_array.append(int(outarray))
                print(unit_all)
                unit_all = sum(unit_array)
                unitall_array.append(unit_all)
                print('そう単位数',unit_all)

            for i in range(0, 5):
                sum_all = 0
                sum_array = []
                queryset = Grade.objects.filter(student_number=serialisersarray[n], evaluation=grade_content[i])
                sumunit = len(queryset)

                if sumunit == 0:
                    numgrade_dict[grade_content[i]] = sum_all

                sum_serializer = Unitserializer(queryset, many=True)

                for z in range(sumunit):
                    sum_unit = list(sum_serializer.data[z].values())
                    sumdata = sum_unit[0]
                    sum_array.append(int(sumdata))
                    sum_all = sum(sum_array)
                    if sum_all == 0:
                        print('正常に動作')
                    numgrade_dict[grade_content[i]] = sum_all
                print(grade_content[i],sum_all,numgrade_dict)

                gradeint_array.append(len(queryset))

            grate = (4.0 * int(numgrade_dict['秀']) + (3.0 * int(numgrade_dict['優'])) + (2.0 * int(numgrade_dict['良'])) + (
                        1.0 * int(numgrade_dict['可']))) / int(unit_all)
            print('学籍番号',serialisersarray[n])
            print('評定平均',grate)
            print(len(serialisersarray))

            grate_array.append(grate)

        print(grate_array)

        print(len(grate_array))

        '''
        学生の成績データの取得
        '''
        queryset = []
        serialiser = []
        for i in range(100):
            queryset.append(Grade.objects.filter(student_number=serialisersarray[i]))
            serialiser.append(Gradeserializers(queryset[i], many=True,))
        Alist = []
        Blist = []
        Clist = []
        Dlist = []

        for i in range(0, 29):
            Alist.append([studentarray[i], serialiser[i].data,[round(grate_array[i],3)]])
        for i in range(30,60):
            Blist.append([studentarray[i], serialiser[i].data,[round(grate_array[i],3)]])
        for i in range(61,87):
            Clist.append([studentarray[i], serialiser[i].data,[round(grate_array[i],3)]])
        for i in range(88,99):
            Dlist.append([studentarray[i], serialiser[i].data,[round(grate_array[i],3)]])


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


class ChangefileStyleViewSet(generics.CreateAPIView):
    serializer_class = Sheetserialiser
    queryset = Sheet.objects.all()

    def post(self,request):
        changesheet = ['student', 'gakka', 'grade', 'subject', 'corce', 'enllold', 'login']
        files = []

        for i in range(7):
            exceldata = pandas.read_excel(request.FILES['changefile'].file,sheet_name=i)
            filename = changesheet[i] + '.csv'
            csvfile = exceldata.to_csv('GradeInquiry/teacher/exelfiles/' + filename, index=False)

        shutil.make_archive('GradeInquiry/teacher/zip', 'zip', root_dir='GradeInquiry/teacher/exelfiles')

        zip_file = zipfile.ZipFile(ZIP_ROOT,mode='r')

        # response =(zip_file, content_type='application/zip')

        # response['Content-Disposition'] = 'attachment; filename="changedata.zip"'

        return FileResponse(open(ZIP_ROOT,mode="rb"),as_attachment=True,filename="changedata.zip")
