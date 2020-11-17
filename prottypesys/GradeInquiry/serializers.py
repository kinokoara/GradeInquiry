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

        '''
        アカウント新規登録の際の処理
        
        usernameが5文字且つ、(bnnnn or Bnnnn)の場合学生であると判断してadmin_flagに0をいれる。
        それ以外の場合には先生であると判断してadmin_flagに1をいれる。   
        例外としてusernameが2文字未満の場合はerrorを登録する    
        '''

        if(len(username) == 5):
            if result1:
                admin_flag = 0
            elif result2:
                admin_flag = 0
            else: admin_flag = 1
        elif(len(username) <= 1):
            admin_flag = 'error'
        else:admin_flag = 1

        return LoginUser.objects.create_user(admin_flag=admin_flag,**validated_data)


class Gradeserializers(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['grade_id','subject_id','student_number','evaluation']

class Loginserializers(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields = ['admin_flag']




