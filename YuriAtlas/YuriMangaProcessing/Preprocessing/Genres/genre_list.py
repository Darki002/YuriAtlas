import json


def get() -> dict[str, int]:
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
