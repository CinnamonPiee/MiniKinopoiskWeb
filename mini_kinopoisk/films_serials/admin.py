from django.contrib import admin
from .models import SearchFilm, SearchSerial


@admin.register(SearchFilm)
class SearchFilmAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "janr", 
        "year", 
        "rating", 
        "country",
    )
    fields = (
        "name",
        "janr",
        "year",
        "country",
        "movie_length",
        "description",
        "rating",
        "age_rating",
        "picture",
    )
    readonly_fields = (
        "name",
        "janr",
        "year",
        "country",
        "movie_length",
        "description",
        "rating",
        "age_rating",
        "picture",
    )
    search_fields = (
        "name",
    )
    ordering = (
        "name",
        "janr",
        "year",
        "country",
        "rating",
        "description",
        "movie_length",
    )


@admin.register(SearchSerial)
class SearchSerialAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "janr", 
        "release_year", 
        "rating", 
        "country",
    )
    fields = (
        "name",
        "janr",
        "rating",
        "release_year",
        "series_length",
        "country",
        "age_rating",
        "description",
        "picture",
    )
    readonly_fields = (
        "name",
        "janr",
        "rating",
        "release_year",
        "series_length",
        "country",
        "age_rating",
        "description",
        "picture",
    )
    search_fields = (
        "name",
    )
    ordering = (
        "name",
        "janr",
        "rating",
        "release_year",
        "series_length",
        "country",
        "description",
    )
