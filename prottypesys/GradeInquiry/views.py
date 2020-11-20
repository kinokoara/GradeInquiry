import logging
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response



from .models import Grade,LoginUser

from .serializers import Userserializers, Gradeserializers,Loginserializers


class CreateUserView(generics.CreateAPIView):
    serializer_class = Userserializers
    permission_classes = (AllowAny,)


# ユーザーの成績表示
# class GradeShowViewSet(generics.ListCreateAPIView):
#     queryset = Grade.objects.all()
#     serializer_class = Gradeserializers
#     '''
#     成績取得のgetメソッドのrequestがきた時の処理の記述
#     '''
#     def list(self, request):
#         user = request.user
#         queryset = Grade.objects.filter(student_number=user)
#         serializer = Gradeserializers(queryset, many=True)
#         return Response(serializer.data)
#
#
# class AllGradeShowViewSet(generics.ListCreateAPIView):
#     queryset = Grade.objects.all()
#     serializer_class = Gradeserializers
#     '''
#     成績取得のgetメソッドのrequestがきた時の処理の記述
#     '''
#
#     def list(self, request):
#         user = request.user
#         queryset = Grade.objects.all()
#         serializer = Gradeserializers(queryset, many=True)
#         return Response(serializer.data)



class LoginView(generics.ListCreateAPIView):

    serializer_class = Loginserializers
    queryset = LoginUser.objects.all()

    def list(self,request):
        user = request.user
        queryset = LoginUser.objects.filter(username=user)
        serializer = Loginserializers(queryset,many=True)
        return Response(serializer.data)
