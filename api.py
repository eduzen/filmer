import requests
from dataclasses import field, dataclass
from settings import OMDb_API_KEY

OMDB_URL = f"http://www.omdbapi.com/?apikey={OMDb_API_KEY}&i=tt3896198&"

@dataclass
class Movie:
    title: str
    year: str
    rated: str
    released: str
    runtime: str
    genre: str
    director: str
    writer: str
    actors: str
    plot: str = ""
    language: str = ""
    awards: str = ""
    country: str = ""
    poster: str = ""
    ratings: str= ""
    metascore: str = ""
    imdbRating: str = ""
    imdbVotes: str = ""
    imdbID: str = ""
    type: str = ""
    dvd: str = ""
    boxOffice: str = ""
    production: str = ""
    website: str = ""
    response: str = ""



def get_movie_data(title):
    """
    Get movie data from OMDb API.
    """
    url = f"{OMDB_URL}&s={title}"
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
    movie = Movie(
        title=data.get("Title", ""),
        year=data.get("Year", ""),
        rated=data.get("Rated", ""),
        released=data.get("Released", ""),
        runtime=data.get("Runtime", ""),
        genre=data.get("Genre", ""),
        director=data.get("Director", ""),
        writer=data.get("Writer", ""),
        actors=data.get("Actors", ""),
        plot=data.get("Plot", ""),
        language=data.get("Language", ""),
        awards=data.get("Awards", ""),
        country=data.get("Country", ""),
        poster=data.get("Poster", ""),
        ratings=data.get("Ratings", ""),
        metascore=data.get("Metascore", ""),
        imdbRating=data.get("imdbRating", ""),
        imdbVotes=data.get("imdbVotes", ""),
        imdbID=data.get("imdbID", ""),
        type=data.get("Type", ""),
        dvd=data.get("DVD", ""),
        boxOffice=data.get("BoxOffice", ""),
        production=data.get("Production", ""),
        website=data.get("Website", "")
    )
    return movie

def parse_search_results(data):
    """
    Parse search results into a list of Movie objects.
    """
    movies = []
    for movie in data["Search"]:
        movies.append(parse_movie(movie))
    return movies


def get_yts_torrent_info(imdb_id):
    try:
        r = requests.get(YTS_API, params={"query_term": imdb_id})
    except requests.exceptions.ConnectionError:
        logger.info("yts api no responde.")
        return None
    r.raise_for_status()

    if r.status_code == 200:
        torrent = r.json()  # <Dar url en lugar de hash.
        try:
            movie = torrent["data"]["movies"][0]["torrents"][0]
            url = movie["url"]
            seeds = movie["seeds"]
            size = movie["size"]
            quality = movie["quality"]

            return url, seeds, size, quality

        except (IndexError, KeyError):
            logger.exception("There was a problem with yts api response")

def main():
    title = input("Enter a movie title: ")
    data = search_movie(title)
    movies = parse_search_results(data)
    for movie in movies:
        print(movie.type, movie.title, movie.year)


if __name__ == "__main__":
    main()