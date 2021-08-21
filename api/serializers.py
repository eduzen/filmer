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
    class Meta:
        model = Movie
        fields = "__all__"


class YtsMovieSerializer(serializers.HyperlinkedModelSerializer):
    imdb_id = serializers.CharField(source="imdb_code")
    poster = serializers.URLField(source="background_image")

    class Meta:
        model = Movie
        fields = ["imdb_id", "title", "year", "poster"]
