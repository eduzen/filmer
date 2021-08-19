from api import parse_search_results, search_movie


def main():
    title = input("Enter a movie title: ")
    data = search_movie(title)
    movies = parse_search_results(data)
    for movie in movies:
        print(vars(movie))


if __name__ == "__main__":
    main()
