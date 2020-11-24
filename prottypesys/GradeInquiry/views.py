import logging
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response



from .models import Grade,LoginUser

from .serializers import Userserializers, Gradeserializers,Loginserializers


class CreateUserView(generics.CreateAPIView):
    serializer_class = Userserializers
    permission_classes = (AllowAny,)





class LoginView(generics.ListCreateAPIView):

    serializer_class = Loginserializers
    queryset = LoginUser.objects.all()

    def list(self,request):
        user = request.user
        queryset = LoginUser.objects.filter(username=user)
        serializer = Loginserializers(queryset,many=True)
        return Response(serializer.data)
