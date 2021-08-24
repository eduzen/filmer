import json
import pathlib

import pytest

from omdb.api import get_movies


@pytest.fixture
def response_fixure():
    current_path = pathlib.Path(__file__).parent.parent.resolve()
    with open(current_path.joinpath("fixtures/response.json")) as f:
        yield json.load(f)


@pytest.mark.vcr()
def test_search_movie():
    movies = get_movies("Star wars")

    assert len(movies) == 10
