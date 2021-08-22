from datetime import datetime
from urllib.parse import urljoin

import requests
from pydantic import BaseModel

from yts.constants import YTS_URL

# from typing import Generic, TypeVar, Optional, List


client = requests.Session()


class Movie(BaseModel):
    background_image: str
    background_image_original = str
    date_uploaded: datetime
    date_uploaded_unix: int
    description_full: str
    genres: list[str]
    id: int
    imdb_code: str
    language: str
    large_cover_image: str
    medium_cover_image: str
    mpa_rating: str
    rating: float
    runtime: int
    slug: str
    small_cover_image: str
    state: str
    summary: str
    synopsis: str
    title: str
    title_english: str
    title_long: str
    torrents: list[dict]
    url: str
    year: int
    yt_trailer_code: str


def get_yts_movie(imdbid: str) -> dict:
    """
    Get movie details from YTS
    :param imdbid:
    :return:
    """
    url = urljoin(YTS_URL, "list_movies.json")
    params = {"query_term": imdbid}
    response = client.get(url, params=params)
    response.raise_for_status()
    return response.json()


def parse_movie(response: dict) -> dict:
    try:
        movie = response["data"]["movies"][0]
        return Movie(**movie)
    except (IndexError, KeyError):
        return {}


def get_movie(imdbid):
    """
    Get movie details
    :param imdbid:
    :return:
    """
    response = get_yts_movie(imdbid)
    return parse_movie(response)
