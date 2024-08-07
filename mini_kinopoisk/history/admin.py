from django.contrib import admin
from .models import HistoryFilm, HistorySerial


@admin.register(HistoryFilm)
class HistoryFilmAdmin(admin.ModelAdmin):
    list_display = (
        "user", 
        "film",
        "created_at",
    )
    fields = (
        "user",
        "film",
        "created_at"
    )
    readonly_fields = (
        "user",
        "film",
        "created_at",
    )
    search_fields = (
        "user",
        "film",
    )
    ordering = (
        "user",
        "film",
        "created_at",
    )



@admin.register(HistorySerial)
class HistorySerialAdmin(admin.ModelAdmin):
    list_display = (
        "user", 
        "serial",
        "created_at",
    )
    fields = (
        "user",
        "serial",
        "created_at",
    )
    readonly_fields = (
        "user",
        "serial",
        "created_at",
    )
    search_fields = (
        "user",
        "serial"
    )
    ordering = (
        "user",
        "serial",
        "created_at",
    )


class UserHistoryFilmAdmin(admin.TabularInline):
    model = HistoryFilm
    fields = (
        "user",
        "film",
    )
    readonly_fields = (
        "user",
        "film",
    )
    ordering = (
        "film",
        "user",
    )
    extra = 0


class UserHistorySerialAdmin(admin.TabularInline):
    model = HistorySerial
    fields = (
        "user",
        "serial",
    )
    readonly_fields = (
        "user",
        "serial",
    )
    ordering = (
        "serial",
        "user",
    )
    extra = 0
