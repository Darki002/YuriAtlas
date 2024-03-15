from YuriMangaListAccess.SpreadSheetAccess import get_unfiltered_genres
from collections import Counter


def get_genre_list():
    unfiltered_genres = get_unfiltered_genres()

    genres_count = Counter(unfiltered_genres)
    genre_list = genres_count.most_common(20)

    genre_list = list(filter(lambda g: g[1] > 10, genre_list))

    print(genre_list)


if __name__ == "__main__":
    get_genre_list()
