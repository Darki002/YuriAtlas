from YuriMangaListAccess.SpreadSheetAccess import get_unfiltered_genres
from collections import Counter
import json

MAX_GENRES = 20
MIN_USAGES = 20


def generate_file():
    unfiltered_genres = get_unfiltered_genres()

    genres_count = Counter(unfiltered_genres)
    genres = genres_count.most_common(MAX_GENRES)

    genres = list(filter(lambda g: g[1] > MIN_USAGES, genres))

    genre_names: list[str] = [genre for genre, count in genres]

    genre_list = [(genre, index) for index, genre in enumerate(genre_names)]

    with open('./genre-list.json', 'w') as outfile:
        json.dump(genre_list, outfile, indent="genres")

    print('Saved to genre-list.json')


if __name__ == "__main__":
    generate_file()
