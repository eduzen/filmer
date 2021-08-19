from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MovieCast(models.Model):
    actor_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=128)
    imdb_id = models.CharField(max_length=10)
    year = models.PositiveSmallIntegerField()
    data = models.JSONField(default=dict)
    poster = models.URLField(max_length=200)
    cast = models.ManyToManyField(MovieCast, related_name="movies")
