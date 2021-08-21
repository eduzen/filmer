from yts.api import search_movie


def main():
    title = input("Enter a movie title: ")
    data = search_movie(title)
    for movie in data:
        print(vars(movie))


if __name__ == "__main__":
    main()
