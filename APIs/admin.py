from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class UserManager(UserAdmin):
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_display = ('id', 'email', 'is_staff', 'is_admin', 'is_active',)
    ordering = ('-date_joined',)
    list_editable = ('is_active',)


admin.site.register(User, UserManager)
