from yuri_manga_processing.manga_source import MangaSource
from yuri_manga_processing.yuri_manga import YuriManga
from dotenv import load_dotenv
import logging
import requests
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

base_path: str = os.path.dirname(__file__)
env_path: str = os.path.join(base_path, ".env")
load_dotenv(env_path)

URL = "https://api.myanimelist.net/v2/users/{username}/mangalist"


def get_manga(manga_id: str) -> tuple[YuriManga, str] | None:

    if manga_id.isdigit() is False:
        return None

    headers = {
        'X-MAL-CLIENT-ID': os.getenv("MAL_CLIENT_ID"),
    }

    params = {
        'sort': 'manga_title',
        'fields': 'list_status, status, nsfw, synopsis, genres, media_type, alternative_titles, main_picture',
        'limit': 100,
        'nsfw': True
    }

    response = requests.get(f"https://api.myanimelist.net/v2/manga/{manga_id}", headers=headers, params=params)

    if response.status_code == 200:

        node = response.json()
        genres = _get_genre_names(node["genres"])
        medium_picture_url = node["main_picture"]["medium"]

        manga = YuriManga(
            manga_id=str(node["id"]),
            source=MangaSource.MyAnimeList,
            title=node["title"],
            alternative_titles=node["alternative_titles"],
            description=node["synopsis"],
            nsfw_level=node["nsfw"],
            genres=genres,
            manga_format=node["media_type"],
            publication=node["status"],
            user_reading_status="",
            user_score=None
        )
        return manga, medium_picture_url
    else:
        logger.error(f"Error while fetching response from MyAnimeList: {response}")
        return None


def get_list(user_name: str) -> list[YuriManga] | None:

    headers = {
        'X-MAL-CLIENT-ID': os.getenv("MAL_CLIENT_ID"),
    }

    params = {
        'sort': 'manga_title',
        'fields': 'list_status, status, nsfw, synopsis, genres, media_type, alternative_titles',
        'limit': 100,
        'nsfw': True
    }

    response = requests.get(URL.format(username=user_name), headers=headers, params=params)

    if response.status_code == 200:
        return _map_response(response.json())
    else:
        logger.error(f"Error while fetching response from MyAnimeList: {response}")
        return None


def _map_response(response) -> list[YuriManga]:
    mangas = response["data"]

    mapped_mangas = []

    for manga in mangas:
        m = _map_manga(manga)
        mapped_mangas.append(m)

    return mapped_mangas


def _map_manga(manga_dict) -> YuriManga:

    node = manga_dict["node"]
    list_status = manga_dict["list_status"]

    genres = _get_genre_names(node["genres"])

    return YuriManga(
        manga_id=str(node["id"]),
        source=MangaSource.MyAnimeList,
        title=node["title"],
        alternative_titles=node["alternative_titles"],
        description=node["synopsis"],
        nsfw_level=node["nsfw"],
        genres=genres,
        manga_format=node["media_type"],
        publication=node["status"],
        user_reading_status=list_status["status"],
        user_score=list_status["score"]
    )


def _get_genre_names(genre_list):
    genre_names = []

    for genre in genre_list:
        genre_names.append(genre["name"])

    return genre_names
