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
        gradeint_array = []

        grade_content = ['秀','優','良','可','不可']



        queryset = Grade.objects.filter(student_number=user)
        all_gradeenv = len(queryset)
        serializer = Gradeserializers(queryset, many=True)


        for i in range(0, 5):
            queryset = Grade.objects.filter(student_number=user, evaluation=grade_content[i])
            gradeint_array.append(len(queryset))


        grate = (4.0 * int(gradeint_array[0]) + (3.0*int(gradeint_array[1])) + (2.0*int(gradeint_array[2])) + (1.0*int(gradeint_array[3]))) /int(all_gradeenv)

        print(grate)



        return Response(
                        [serializer.data,grate]
                        )

