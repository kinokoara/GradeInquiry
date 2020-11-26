from django.contrib import admin
from .models import LoginUser,Student,Subject,Grade,Enrolled,Depart,Course
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['username', 'email']
    fieldsets = (
        (None, {'fields': ('email', 'password','admin_flag')}),
        (_('Personal Info'), {'fields': ('username',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2','admin_flag')
        }),
    )

class DepartAdmin(admin.ModelAdmin):
    list_display = ('depart_id', 'depart_name')
    ordering = ['depart_id', ]

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'course_name', 'depart_id')
    search_fields = ('course_id', 'course_name')
    ordering = ['depart_id', ]


class GradeAdmin(admin.ModelAdmin):
    list_display = ('grade_id', 'subject_id','student_number', 'evaluation')
    search_fields = ('student_number', )
    ordering = ['student_number', ]


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_number', 'student_name', 'class_number','enrolled_id')
    search_fields = ('student_name', 'student_number')
    ordering = ['student_number', ]


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'dividend_period', 'units')
    search_fields = ('subject_name',)
    ordering = ['units', ]


admin.site.register(LoginUser, UserAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Depart, DepartAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Enrolled)






