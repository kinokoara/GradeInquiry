from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response

from GradeInquiry.models import Grade
from GradeInquiry.serializers import Gradeserializers,Unitserializer


class GradeShowViewSet(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = Gradeserializers
    '''
    成績取得のgetメソッドのrequestがきた時の処理の記述
    '''
    def list(self, request):
        user = request.user
        gradeint_array = []
        unit_array = []
        grade_content = ['秀','優','良','可','不可']



        queryset = Grade.objects.filter(student_number=user,)
        data_int = len(queryset)
        serializer = Gradeserializers(queryset, many=True)
        unit_serializer = Unitserializer(queryset,many=True)
        numgrade_dict = {}

        for n in range(data_int):
            unit_num = (list(unit_serializer.data[n].values()))
            outarray = unit_num[0]
            unit_array.append(int(outarray))
            allunit = sum(unit_array)
        print(allunit)

        for i in range(0, 5):
            sum_all = 0
            sum_array = []
            queryset = Grade.objects.filter(student_number = user, evaluation=grade_content[i])
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
            print(grade_content[i], sum_all, numgrade_dict)

            gradeint_array.append(len(queryset))

        grate = (4.0 * int(numgrade_dict['秀']) + (3.0 * int(numgrade_dict['優'])) + (2.0 * int(numgrade_dict['良'])) + (
                1.0 * int(numgrade_dict['可']))) / int(allunit)

        print(grate)



        return Response(
                        [serializer.data,round(grate,3)]
                        )

