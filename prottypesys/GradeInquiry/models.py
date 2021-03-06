from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self,username,password=None,**extra_fields):
        if not username:
            raise ValueError('学籍番号の入力は必須です')
        user = self.model(username=username,**extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self,username,password,):
        user = self.create_user(username,password,)

        user.is_superuser = True

        user.is_staff = True

        user.save(using=self._db)

        return user

class LoginUser(AbstractBaseUser,PermissionsMixin):#ログインテーブル

    username = models.CharField(max_length=255, unique=True,default="")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(max_length=255,)
    admin_flag = models.IntegerField(default=0)
    secret_key = models.IntegerField(default=0)
    objects = UserManager()
    USERNAME_FIELD = 'username'


    def __str__(self):
        return self.username


class Depart (models.Model):#学科マスタ
    depart_id = models.CharField('学科ID',max_length=10,primary_key=True)
    depart_name = models.CharField('学科名',max_length=255)

    def __str__(self):
        return self.depart_id


class Course (models.Model):#コースマスタ
    course_id = models.CharField('コースID',max_length=10,primary_key=True)
    course_name =models.CharField('コース名',max_length=255)
    depart_id = models.CharField('学科ID',max_length=10)

    def __str__(self):
        return self.course_id

class Student(models.Model):#学籍マスタ
    student_number = models.CharField('学籍番号',max_length=5,primary_key=True)
    student_name = models.CharField('氏名',max_length=20)
    class_number = models.CharField('クラス番号',max_length=6)
    couse_id = models.CharField('コースID',max_length=10,null=True)
    enrolled_id = models.CharField('在籍ID',max_length=10)



    def __str__(self):
        return self.student_number

class Subject(models.Model):#科目テーブル
    subject_id = models.CharField('科目番号',blank=True,max_length=7,primary_key=True)
    subject_name = models.CharField('科目名',max_length=25)
    units = models.CharField('単位数',max_length=2)
    dividend_period = models.CharField('配当期',max_length=8)
    lecture_name = models.CharField('担当者',max_length=25,default="")

    def __str__(self):
        return self.subject_name

class Grade(models.Model):#成績テーブル

    grade_id = models.CharField('成績ID',blank=True,max_length=10,primary_key=True)
    evaluation = models.CharField('評価',blank=True,max_length=2,)

    subject_id = models.ForeignKey(Subject,verbose_name='科目番号',on_delete=models.CASCADE ,null=True,blank=True)


    student_number = models.CharField('学籍番号',blank=True,max_length=5)

    def subject_name(self):
        id = self.subject_id
        queryset = Subject.objects.get(subject_name=id)
        return queryset.subject_name

    def Dividend_period(self):
        id = self.subject_id
        queryset = Subject.objects.get(subject_name=id)
        return queryset.dividend_period

    def Units(self):
        id = self.subject_id
        queryset = Subject.objects.get(subject_name=id)
        return queryset.units

    def lecture_name(self):
        id = self.subject_id
        queryset = Subject.objects.get(subject_name=id)
        return queryset.lecture_name

    def __str__(self):
        return (self.student_number)

class Enrolled(models.Model):
    enrolled_id = models.CharField(max_length=10)
    enrolled_status = models.CharField(max_length=2)
    enrolled_date = models.DateTimeField()
    def __str__(self):
        return self.enrolled_id


class Poster(models.Model):
    poster_id = models.AutoField('投稿ID',primary_key=True)
    poster_name = models.CharField('投稿者',max_length=20,blank=True)
    poster_content = models.CharField('投稿内容',max_length=250,blank=True)
    post_data = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.poster_name

class Sheet(models.Model):
    changefile = models.FileField(blank=False,null=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.changefile







