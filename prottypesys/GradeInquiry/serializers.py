from rest_framework import serializers
import random
from .models import LoginUser,Grade,Poster,Sheet
import re



class Userserializers(serializers.ModelSerializer):

    class Meta:
        model = LoginUser
        fields = ('username', 'password',)

    def create(self,validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        # pattern1 = '^b.?[0-9]{4}'
        pattern = '^[A-D].?[0-9]{4}'
        # result1 = re.fullmatch(pattern1,username)
        result2 = re.fullmatch(pattern,username)

        key = random.randint(100000000000,999999999999)

        key_array = []

        for i in key_array:
            if i == key_array:
                key = random.randint(100000000000, 999999999999)

        '''
        アカウント新規登録の際の処理
        
        usernameが5文字且つ、(bnnnn or Bnnnn)の場合学生であると判断してadmin_flagに0をいれる。
        それ以外の場合には先生であると判断してadmin_flagに1をいれる。   
        例外としてusernameが2文字未満の場合はerrorを登録する    
        '''

        if(len(username) == 5):
            if result2:
                admin_flag = 0

            else: admin_flag = 1
        elif(len(username) <= 1):
            admin_flag = 'error'
        else:admin_flag = 1

        return LoginUser.objects.create_user(admin_flag=admin_flag,secret_key=key,**validated_data)

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])

        instance.save()

        return instance


class Gradeserializers(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['grade_id','subject_name','Dividend_period','evaluation','Units','lecture_name']

class Loginserializers(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields = ['secret_key','admin_flag']

class Gradestudentseriarizer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['student_number']


class Postserialiser(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = ['poster_id','poster_name','poster_content','post_data']

class Unitserializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['Units']

class Postuserserialiser(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = ['poster_name']

class Sheetserialiser(serializers.ModelSerializer):


    class Meta:
        model = Sheet
        fields = ['changefile']

class SecretSeriarizers(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields = ['id']

class Changepwseriarizer(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields = ['password']




