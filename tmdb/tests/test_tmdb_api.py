import pytest

from tmdb.api import tmdb_movie_search, tmdb_trending_movies


@pytest.mark.vcr()
def test_tmdb_trending_movies():
    """
    Test the tmdb_trending_movies function.
    """
    MOVIE_KEYS = {
        "adult",
        "backdrop_path",
        "belongs_to_collection",
        "budget",
        "genres",
        "homepage",
        "id",
        "imdb_id",
        "original_language",
        "original_title",
        "overview",
        "popularity",
        "poster_path",
        "production_companies",
        "production_countries",
        "release_date",
        "revenue",
        "runtime",
        "spoken_languages",
        "status",
        "tagline",
        "title",
        "video",
        "vote_average",
        "vote_count",
        "poster_link",
        "imdb_link",
    }
    response = tmdb_trending_movies()
    assert response is not None
    for movie in response:
        result = set(movie.keys())
        assert result.issubset(MOVIE_KEYS)


@pytest.mark.vcr()
def test_tmdb_movie_search():
    """
    Test the tmdb_movie_search function.
    """
    MOVIE_KEYS = {
        "adult",
        "backdrop_path",
        "genre_ids",
        "id",
        "original_language",
        "original_title",
        "overview",
        "popularity",
        "poster_path",
        "release_date",
        "title",
        "video",
        "vote_average",
        "vote_count",
    }
    # Test the function.
    response = tmdb_movie_search("Star wars")
    for movie in response:
        assert set(movie.keys()) == MOVIE_KEYS
