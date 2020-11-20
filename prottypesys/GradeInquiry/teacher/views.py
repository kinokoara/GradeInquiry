from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response

from GradeInquiry.models import Grade
from io import TextIOWrapper

import csv


# ------------------------------------------------------------------
from GradeInquiry.serializers import Gradeserializers


def file_upload(request):
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

        return HttpResponseRedirect('success/url/')

    else:
        return render(request, 'file_upload.html')




class AllGradeShowViewSet(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = Gradeserializers
    '''
    成績取得のgetメソッドのrequestがきた時の処理の記述
    '''

    def list(self, request):
        user = request.user
        queryset = Grade.objects.all()
        serializer = Gradeserializers(queryset, many=True)
        return Response(serializer.data)

# #
# def success(request):
#     str_out = "Success!<p />"
#     str_out += "成功<p />"
#     return HttpResponse(str_out)



