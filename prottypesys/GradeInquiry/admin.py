from django.contrib import admin
from .models import LoginUser,Student,Subject,Grade,Enrolled,Depart,Course,Poster
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['username', 'email']
    fieldsets = (
        (None, {'fields': ('password','admin_flag')}),
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

admin.site.register(LoginUser, UserAdmin)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Depart)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Enrolled)
admin.site.register(Poster)





