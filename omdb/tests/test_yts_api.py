import json
import pathlib

import pytest

from omdb.api import get_movies


@pytest.fixture
def response_fixure():
    current_path = pathlib.Path(__file__).parent.parent.resolve()
    with open(current_path.joinpath("fixtures/response.json")) as f:
        yield json.load(f)


def test_search_movie(mocker, response_fixure):
    mocker.patch("omdb.api.requests.get", return_value=response_fixure)
    movies = get_movies("Star wars")

    assert len(movies) == 10
