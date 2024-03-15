import genrated_genre_list
import json
import os


def get() -> dict[str, int] | None:
    if not os.path.exists('genre_list.json'):
        print('genre-list.json not set up')
        try:
            genrated_genre_list.generate_file()
        except Exception as e:
            print(f"Couldn't generate file! {e}")
            return None

        print("genre-list.json generated")

    with open('genre-list.json', "r") as outfile:
        data = json.load(outfile)
        return data["genres"]


GENRES = {
    'romance': 0,
    'drama': 1,
    'comedy': 2,
    'slice of life': 3,
    'fantasy': 4,
    'sci-fi': 5,
    'mystery': 6,
    'horror': 7,
    'sports': 8,
    'action': 9,
    'adventure': 10,
    'supernatural': 11
}


def get_manual_list() -> dict[str, int]:
    return GENRES.copy()
