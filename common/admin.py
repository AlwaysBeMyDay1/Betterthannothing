from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =(
        'id', 'username','email','password','last_login',
        'nickname','gender', 'mileage', 'level', 'content'
    )

