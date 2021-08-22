from enum import Enum

import requests
from pydantic import BaseModel, ValidationError

from filmer.settings import OMDb_API_KEY

OMDB_URL = f"http://www.omdbapi.com/?apikey={OMDb_API_KEY}&i=tt3896198&"


client = requests.Session()


class OmdbType(str, Enum):
    movie = "movie"
    serie = "series"
    episode = "episode"


class OmdbMovie(BaseModel):
    title: str
    year: str
    imdbid: str
    type: OmdbType
    poster: str

    class Config:
        use_enum_values = True


def get_movie_data(title, page=1, type="movie"):
    """
    Get movie data from OMDb API.
    """
    url = f"{OMDB_URL}&s={title}&page={page}&type={type}"
    response = client.get(url)
    response.raise_for_status()
    data = response.json()
    return data


def get_tv_data(title, page=1, type="serie"):
    """
    Get movie data from OMDb API.
    """
    url = f"{OMDB_URL}&s={title}&page={page}&type={type}"
    response = client.get(url)
    response.raise_for_status()
    data = response.json()
    return data


def search_movie(title: str) -> dict:
    """
    Search for a movie and get all possible matches by OMDB api.
    """
    url = f"{OMDB_URL}&s={title}&type={OmdbType.movie}"
    response = client.get(url)
    response.raise_for_status()
    data = response.json()
    return data


def _parse_movie(data):
    """
    Parse movie data into a Movie object.
    """
    to_lower_case = {k.lower(): v for k, v in data.items()}
    try:
        movie = OmdbMovie(**to_lower_case)
        movie.year = movie.year.replace("-", "").strip()
    except ValidationError:
        raise Exception(f"Could not parse movie data: {to_lower_case}")
    return movie

    return movie


def parse_search_results(data: dict) -> list[OmdbMovie]:
    """
    Parse search results into a list of Movie objects.
    """
    movies = []
    for movie in data["Search"]:
        movies.append(_parse_movie(movie))
    return sorted(movies, key=lambda m: m.year, reverse=True)


def get_movies(title: str) -> list[OmdbMovie]:
    """
    Get all movies by title.
    """
    raw_data = search_movie(title)
    movies = parse_search_results(raw_data)
    return movies
