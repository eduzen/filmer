import logging

from django import template
from django.utils.safestring import mark_safe

register = template.Library()
logger = logging.getLogger(__name__)


def get_title(movie):
    return movie["title"] or movie["original_title"]


@register.simple_tag
def poster(movie):

    return mark_safe(f"<img src='{movie['poster_link']}' class='card-img-top' alt='{get_title(movie)}'>")


@register.simple_tag
def title(movie):
    return mark_safe(f"<h5 class='card-title'>{get_title(movie)}</h5>")


@register.simple_tag
def overview(movie):
    return mark_safe(f"<p class='card-text'>{movie['overview']}</p>")


@register.simple_tag
def genres(movie):
    genres = [m.keys for m in movie["genres"]]
    logger.warning(genres)
    return mark_safe(f"<p class='card-text'>{genres}</p>")


@register.simple_tag
def imdb_link(movie):
    return mark_safe(f"<a href='{movie['imdb_link']}' class='card-link'>IMDB</a>")


@register.simple_tag
def release_date(movie):
    return mark_safe(f"<p>{movie['release_date']}</p>")


@register.simple_tag
def get_api_view(movie):
    return mark_safe(f"<a href='/api/v1/movies/{movie['imdb_id']}' class='btn btn-primary'>API</a>")
