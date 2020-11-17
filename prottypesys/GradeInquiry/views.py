import logging
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Grade

from .serializers import Userserializers, Gradeserializers


class CreateUserView(generics.CreateAPIView):
    serializer_class = Userserializers
    permission_classes = (AllowAny,)


# ユーザーの成績表示
class GradeShowViewSet(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = Gradeserializers
    permission_classes = (AllowAny,)

    def list(self, request):
        user = self.headers.get('username')
        logging.info(user)
        queryset = Grade.objects.filter(student_number=user)
        logging.debug(queryset)
        serializer = Gradeserializers(queryset, many=True)
        return Response(serializer.data)
