from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response

from GradeInquiry.models import Grade
from GradeInquiry.serializers import Gradeserializers


class GradeShowViewSet(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = Gradeserializers
    '''
    成績取得のgetメソッドのrequestがきた時の処理の記述
    '''
    def list(self, request):
        user = request.user
        queryset = Grade.objects.filter(student_number=user)
        serializer = Gradeserializers(queryset, many=True)
        return Response(serializer.data)
