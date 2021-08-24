import json
import pathlib

import pytest

from yts.api import get_movie


@pytest.fixture
def response_fixure():
    current_path = pathlib.Path(__file__).parent.parent.resolve()
    with open(current_path.joinpath("fixtures/response.json")) as f:
        yield json.load(f)


@pytest.mark.vcr()
def test_get_movie():
    movie = get_movie(imdbid="tt3748528")

    assert movie.title == "Rogue One: A Star Wars Story"
    assert movie.year == 2016
    assert movie.rating == 7.8
