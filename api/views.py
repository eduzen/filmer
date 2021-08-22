import logging

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .models import Movie
from .serializers import GroupSerializer, MovieSerializer, UserSerializer

logger = logging.getLogger(__name__)


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
    lookup_field = "imdbid"

    def get_queryset(self):
        if title := self.request.query_params.get("search"):
            return Movie.omdb.search(title)
        else:
            return super().get_queryset()

    def get_object(self):
        if lookup_field := self.kwargs.get(self.lookup_field):
            logger.debug("debug %s", lookup_field)
            return Movie.yts.search(lookup_field)

        return super().get_object()
