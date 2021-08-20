from django.contrib import admin

from .models import Movie, MovieCast


@admin.register(MovieCast)
class MovieCastAdmin(admin.ModelAdmin):
    list_display = ("id", "actor_name", "role")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "imdb_id", "year", "data", "poster")
    raw_id_fields = ("cast",)
