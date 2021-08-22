import logging
from urllib.parse import urljoin

from django.contrib.sites.models import Site
from django.db import models
from django.urls import reverse

from omdb.api import get_movies
from yts.api import get_movie as get_yts_movie

logger = logging.getLogger(__name__)


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MovieCast(models.Model):
    actor_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)


class OmdbManager(models.Manager):
    def filter(self, **kwargs):
        logger.debug("debug %s", kwargs)
        return self.search(**kwargs)

    def search(self, title):
        movies = get_movies(title)
        movies = [self.model(**m.dict()) for m in movies]
        return movies


class YtsManager(models.Manager):
    def filter(self, **kwargs):
        logger.debug("debug %s", kwargs)
        return self.search(**kwargs)

    def search(self, imdbid):
        movie = get_yts_movie(imdbid)
        movie = self.model(title=movie.title, imdbid=imdbid, year=movie.year, data=movie.dict())
        return movie


class Movie(models.Model):
    title = models.CharField(max_length=128)
    imdbid = models.CharField(max_length=10)
    year = models.CharField(max_length=15)
    data = models.JSONField(default=dict, blank=True)
    poster = models.URLField(max_length=200, blank=True)
    cast = models.ManyToManyField(MovieCast, related_name="movies", blank=True)
    type = models.CharField(max_length=10, default="movie")

    omdb = OmdbManager()
    yts = YtsManager()
    objects = models.Manager()

    @classmethod
    def search(cls, title):
        movies = get_movies(title)
        return movies

    def get_absolute_url(self):
        domain = Site.objects.get_current().domain
        relative_uri = reverse("movie-detail", kwargs={"imdbid": self.imdbid})
        absolute_uri = urljoin(f"http://{domain}", relative_uri)
        return absolute_uri

    @property
    def imdburl(self):
        return f"https://www.imdb.com/title/{self.imdbid}"

    def __str__(self):
        return f"{self.title} - {self.imdbid}"

    class Meta:
        ordering = ["-year", "title"]
        # abstract = True
