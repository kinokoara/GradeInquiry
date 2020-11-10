from rest_framework import serializers
import random
from .models import LoginUser,Grade
import re



class Userserializers(serializers.ModelSerializer):

    class Meta:
        model = LoginUser
        fields = ('username', 'password',)

    def create(self,validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        pattern1 = '^b.?[0-9]{4}'
        pattern2 = '^B.?[0-9]{4}'
        result1 = re.fullmatch(pattern1,username)
        result2 = re.fullmatch(pattern2,username)
        if(len(username) == 5):
            if result1:
                admin_flag = random.randint(1,50)
            elif result2:
                admin_flag = random.randint(1,50)
            else: admin_flag = random.randint(51,100)
        elif(len(username) <= 5):
            admin_flag = 101
        else:admin_flag = random.randint(51,100)

        return LoginUser.objects.create_user(admin_flag=admin_flag,**validated_data)


class Gradeserializers(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['grade_id','subject_id','student_number','evaluation']



    def list(self):

        return Grade.objects.filter(student_number='b9110')




