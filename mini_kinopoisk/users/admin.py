from django.contrib import admin
from .models import User
from history.admin import UserHistoryFilmAdmin, UserHistorySerialAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username", 
        "is_superuser", 
        "is_staff", 
        "is_active", 
        "first_name", 
        "last_name", 
        "email", 
        "phone_number", 
        "last_login",
    )
    fields = (
        "password", 
        "last_login", 
        "is_superuser", 
        "username", 
        "first_name", 
        "last_name", 
        "email", 
        "is_staff", 
        "is_active", 
        "date_joined", 
        "telegram_id", 
        "phone_number", 
        "image",
    )
    readonly_fields = (
        "password",
        "last_login",
        "is_superuser",
        "is_staff",
        "is_active",
        "date_joined",
        "telegram_id",
        "image",
    )
    search_fields = (
        "username",
    )
    ordering = (
        "username",
        "date_joined",
        "last_login",
        "first_name",
        "last_name",
        "email",
    )
    inlines = (UserHistoryFilmAdmin, UserHistorySerialAdmin)
