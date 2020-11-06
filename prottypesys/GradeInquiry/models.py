from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

import pdb
class UserManager(BaseUserManager):
    def create_user(self,username,password=None,**extra_fields):
        if not username:
            raise ValueError('学籍番号の入力は必須です')
        user = self.model(username=username,**extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self,username,password):
        user = self.create_user(username,password)

        user.is_superuser = True

        user.is_staff = True

        user.save(using=self._db)

        return user

class LoginUser(AbstractBaseUser,PermissionsMixin):#ログインテーブル

    username = models.CharField(max_length=255, unique=True,default="")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(max_length=255,)
    admin_flag = models.IntegerField(default=0);
    objects = UserManager()
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username


class Depart (models.Model):#学科マスタ
    depart_id = models.CharField(max_length=10,primary_key=True)
    depart_name = models.CharField(max_length=255)

    def __str__(self):
        return self.depart_id


class Course (models.Model):#コースマスタ
    course_id = models.CharField(max_length=10,primary_key=True)
    course_name =models.CharField(max_length=255)
    depart_id = models.CharField(max_length=10)

    def __str__(self):
        return self.course_id

class Student(models.Model):#学籍マスタ
    student_number = models.CharField(max_length=5,primary_key=True)
    student_name = models.CharField(max_length=20)
    class_number = models.CharField(max_length=6)
    enrolled_id = models.CharField(max_length=10)
    couse_id = models.CharField(max_length=10,null=True)
    birthday = models.DateTimeField(null=True)

    def __str__(self):
        return self.student_number

class Grade(models.Model):
    grade_id = models.CharField(max_length=10,primary_key=True)
    subject_id = models.CharField(max_length=7)
    student_number = models.CharField(max_length=5)
    evaluation = models.CharField(max_length=2)

    def __str__(self):
        return self.grade_id

class Subject(models.Model):
    subject_id = models.CharField(max_length=7,primary_key=True)
    subject_name = models.CharField(max_length=25)
    dividend_period = models.CharField(max_length=8)
    units = models.CharField(max_length=2)

    def __str__(self):
        return self.subject_id

class Enrolled(models.Model):
    enrolled_id = models.CharField(max_length=10)
    enrolled_status = models.CharField(max_length=2)
    enrolled_date = models.DateTimeField()
    def __str__(self):
        return self.enrolled_id








