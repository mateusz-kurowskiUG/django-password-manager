from django.contrib import admin
from .models import Accounts,User_avatar
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


admin.site.register(Accounts)
admin.site.register(User_avatar)