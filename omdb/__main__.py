from api import get_movies


def main():
    title = input("Enter a movie title: ")
    movies = get_movies(title)
    for movie in movies:
        print(movie)


if __name__ == "__main__":
    main()
