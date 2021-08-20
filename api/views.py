from django.contrib.auth.models import Group, User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets

from omdb.api import search_movie

from .models import Movie
from .serializers import GroupSerializer, MovieSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["title"]
    search_fields = ["@title"]

    def get_queryset(self):
        queryset = super().get_queryset()
        if queryset.count() == 0:
            print("ada", self.request.kwargs["title"])
            movie = search_movie(self.request.kwargs["title"])
            print(movie)
            # @Movie.objects.create(**movie)
        return queryset


"tt0116282"
"https://yts.mx/api/v2/list_movies.json"
