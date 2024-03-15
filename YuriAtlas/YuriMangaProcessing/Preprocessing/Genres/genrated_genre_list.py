import os

from YuriMangaListAccess.SpreadSheetAccess import get_unfiltered_genres
import logging
from collections import Counter
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

base_path: str = os.path.dirname(__file__)
FILE_PATH: str = os.path.join(base_path, "genre-list.json")

MAX_GENRES = 20
MIN_USAGES = 10


def generate_file() -> None:
    logger.info("Starting to generate genres list...")
    unfiltered_genres = get_unfiltered_genres()

    if unfiltered_genres is None:
        logger.info("No genres found!")
        return

    logger.info("Fetched genres from spreadsheet")

    genres_count = Counter(unfiltered_genres)
    genres = genres_count.most_common(MAX_GENRES)

    genres = list(filter(lambda g: g[1] > MIN_USAGES, genres))
    genre_names: list[str] = [genre for genre, count in genres]
    genre_list = [{"Name": genre, "Index": index} for index, genre in enumerate(genre_names)]

    try:
        with open(FILE_PATH, 'w') as outfile:
            json.dump(genre_list, outfile, indent=4)
        logger.info('Saved to genre-list.json')
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    generate_file()
