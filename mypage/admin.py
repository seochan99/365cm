from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

admin.site.register(Profile)

class ProfileInline(admin.StackedInline): 
    model = Profile
    con_delete = False                    # 프로필을 아예 없앨 수 없게 하는 속성(한번 만들면 지우는건 이상하니까)


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)