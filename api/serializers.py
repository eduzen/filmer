from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import Movie


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.URLField(source="get_absolute_url", read_only=True)

    class Meta:
        model = Movie
        fields = ["url", "imdbid", "title", "year", "poster", "imdburl", "data"]


class YtsMovieSerializer(serializers.HyperlinkedModelSerializer):
    imdbid = serializers.CharField(source="imdb_code")
    poster = serializers.URLField(source="background_image")

    class Meta:
        model = Movie
        fields = ["imdbid", "title", "year", "poster", "imdburl"]
