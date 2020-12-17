import logging
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Grade,LoginUser,Poster

from .serializers import Userserializers, Gradeserializers,Loginserializers,Postserialiser


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
        value = serializer.data[0]
        print(value)
        return Response(serializer.data)


class AddPostcontentView(generics.ListCreateAPIView):
    serializer_class = Postserialiser
    queryset = Poster.objects.all()

    def post(self,request):
        user = request.user
        content = request.data['poster_content']
        date = request.data['post_data']
        pos = Poster()
        pos.poster_name = user
        pos.poster_content = content
        pos.post_data = date
        pos.save()
        return Response('ok add!!')

    def list(self,request):
        queryset = Poster.objects.all()
        serializer = Postserialiser(queryset,many=True)

        return Response(serializer.data)


class DeletepostView(generics.DestroyAPIView,generics.ListAPIView):
        serializer_class = Postserialiser
        queryset = Poster.objects.all()

        def list(self,request,pk):
            queryset = Poster.objects.filter(poster_id=pk)
            serializer = Postserialiser(queryset, many=True)
            return Response(serializer.data)

        def delete(self, request, pk, format=None):
            user = request.user
            queryset = LoginUser.objects.filter(username=user)
            serializer = Loginserializers(queryset,many=True)
            flag_data = (list(serializer.data[0].values()))
            flag = flag_data[0]
            print(flag)

            if flag == 1:
                poster = Poster.objects.filter(poster_id=pk)
                poster.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response('You do not have permission to delete!!!')