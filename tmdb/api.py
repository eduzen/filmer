import enum
import logging

import requests
import tmdbsimple as tmdb

from filmer.settings import TMDB_API_KEY

tmdb.REQUESTS_SESSION = requests.Session()
tmdb.API_KEY = TMDB_API_KEY
logger = logging.getLogger(__name__)


class TimeWindow(enum.Enum):
    WEEK = "week"
    DAY = "day"

    def __str__(self) -> str:
        return self.value


class MediaType(enum.Enum):
    MOVIE = "movie"
    TV = "tv"
    PERSON = "person"
    ALL = "all"


def tmdb_movie_search(query: str) -> list:
    search = tmdb.Search()
    response = search.movie(query=query)
    if not response["results"]:
        return []

    return response["results"]


def get_movie_detail(pk: int) -> dict:
    try:
        movie_data = tmdb.Movies(pk).info()
    except Exception:
        logger.exception("Error getting movie detail")
        return {}
    try:
        movie_data["imdb_link"] = f"https://www.imdb.com/title/{movie_data['imdb_id']}"
        movie_data["poster_link"] = f"https://image.tmdb.org/t/p/w342{movie_data['poster_path']}"
    except KeyError:
        pass

    return movie_data


def tmdb_trending_movies(media_type: MediaType = MediaType.MOVIE, time_window: TimeWindow = TimeWindow.WEEK) -> list:
    try:
        trending = tmdb.Trending(time_window=time_window, media_type=media_type)
        response = trending.info(page=1)
        return (get_movie_detail(movie.get("id")) for movie in response["results"])
    except Exception:
        logger.exception("Error getting trending movies")
        return []
