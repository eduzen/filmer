import os

import requests

try:
    from filmer.settings import OMDb_API_KEY
except ModuleNotFoundError:
    OMDb_API_KEY = os.getenv("OMDb_API_KEY", "fake")

from types import SimpleNamespace

OMDB_URL = f"http://www.omdbapi.com/?apikey={OMDb_API_KEY}&i=tt3896198&"


def get_movie_data(title, page=1, type="movie"):
    """
    Get movie data from OMDb API.
    """
    url = f"{OMDB_URL}&s={title}&page={page}&type={type}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data


def get_tv_data(title, page=1, type="serie"):
    """
    Get movie data from OMDb API.
    """
    url = f"{OMDB_URL}&s={title}&page={page}&type={type}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data


def search_movie(title):
    """
    Search for a movie and get its id.
    """
    url = f"{OMDB_URL}&s={title}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data


def parse_movie(data):
    """
    Parse movie data into a Movie object.
    """
    movie = SimpleNamespace(**{k.lower(): v for k, v in data.items()})
    return movie


def parse_search_results(data):
    """
    Parse search results into a list of Movie objects.
    """
    movies = []
    print(data)
    for movie in data["Search"]:
        movies.append(parse_movie(movie))
    return movies
