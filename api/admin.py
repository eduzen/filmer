from django.contrib import admin

from .models import Movie, MovieCast


@admin.register(MovieCast)
class MovieCastAdmin(admin.ModelAdmin):
    list_display = ("id", "actor_name", "role")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "imdbid", "year", "data", "poster")
    raw_id_fields = ("cast",)
