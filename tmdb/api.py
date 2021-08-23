import enum
from filmer.settings import TMDB_API_KEY
import tmdbsimple as tmdb

tmdb.API_KEY = TMDB_API_KEY

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


def tmdb_movie_search(query:str) -> list:
    search = tmdb.Search()
    response = search.movie(query=query)
    if not response["results"]:
        return []

    return response["results"]

def get_movie_detail(pk):
    return tmdb.Movies(pk)

def tmdb_trending_movies(media_type:MediaType = MediaType.MOVIE, time_window:TimeWindow=TimeWindow.WEEK) -> list:
    trending = tmdb.Trending(time_window=time_window, media_type=media_type)
    response = trending.info(page=1)
    return (get_movie_detail(movie.get("id")) for movie in response["results"])
