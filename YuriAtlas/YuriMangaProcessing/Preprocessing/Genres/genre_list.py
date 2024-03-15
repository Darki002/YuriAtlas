import genrated_genre_list
import logging
import json
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get() -> dict[str, int] | None:
    if not os.path.exists('genre_list.json'):
        logger.warning('genre-list.json not set up')
        try:
            genrated_genre_list.generate_file()
        except Exception as e:
            logger.error(f"Couldn't generate file! {e}")
            return None

        logger.info("genre-list.json generated")

    with open('genre-list.json', "r") as outfile:
        data = json.load(outfile)
        return data["genres"]
