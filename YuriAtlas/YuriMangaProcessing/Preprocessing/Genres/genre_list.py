import logging
import json
import os

base_path: str = os.path.dirname(__file__)
FILE_PATH: str = os.path.join(base_path, "genre-list.json")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_genre_list() -> dict[str, int] | None:
    if not os.path.exists(FILE_PATH):
        raise FileNotFoundError(FILE_PATH)

    with open(FILE_PATH, "r") as outfile:
        data = json.load(outfile)
        genre_list = [(genre["Name"], genre["Index"]) for genre in data]
        return dict(genre_list)
