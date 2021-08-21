from urllib.parse import urljoin

import requests

from .constants import YTS_URL

client = requests.Session()


def get_movie(imdb_id):
    """
    Get movie details
    :param imdb_id:
    :return:
    """
    url = urljoin(YTS_URL, "list_movies.json")
    params = {"query_term": imdb_id}
    response = client.get(url, params=params)
    return response.json()
