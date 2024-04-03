from yuri_manga_processing.manga_source import MangaSource
from yuri_manga_processing.yuri_manga import YuriManga
from data_access.yuri_manga_spreadsheet.levensteins_distance import distance
from google.oauth2 import service_account
import gspread
import logging
import os.path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

base_path: str = os.path.dirname(__file__)
FILE_PATH: str = os.path.join(base_path, "yuriatlas-ba7416ea8160.json")


def _get_worksheet(worksheet_index: int):
    credentials = service_account.Credentials.from_service_account_file(
        FILE_PATH,
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )

    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_key('10q6IqRr9kxtpZ4TKixNIEzRZXcqP_2o-mbPnt8e5vCA')
    return spreadsheet.get_worksheet(worksheet_index)


def get_all_genres() -> list[str] | None:
    try:
        worksheet = _get_worksheet(2)  # 2 = worksheet "Data"
        genres = worksheet.col_values(19)  # 19 = Col "S"
        return genres
    except Exception as e:
        logger.error(e)
        return None


def get_unfiltered_genres() -> list[str] | None:
    try:
        worksheet = _get_worksheet(2)  # 2 = worksheet "Data"
        genres = worksheet.col_values(18)  # 18 = Col "R"
        return genres
    except Exception as e:
        logger.error(e)
        return None


def get_all():
    try:
        worksheet = _get_worksheet(1)  # 2 = worksheet "List"
        rows = worksheet.get_all_values()
        return [_map_to_yuri_mang(row, index) for index, row in enumerate(rows)]

    except Exception as e:
        logger.error(f"Failed to retrieve data. Error: {e}")
        return None


def get_by_id(manga_id: str) -> YuriManga | None:
    if manga_id.isdigit() is False:
        return None
    manga_id = int(manga_id)

    mangas = get_all()
    return mangas[manga_id]


def get_by_name(manga_name: str):
    try:
        rows = get_all()
        if len(rows) == 0:
            return None

        mangas = filter(lambda m: m.title == manga_name, rows)
        return next(mangas, None)

    except Exception as e:
        logger.error(f"Failed to retrieve data. Error: {e}")
        return None


def search_by_name(manga_name: str, genres: list[str] | None, nsfw_enabled: bool):
    try:
        rows: list[YuriManga] = get_all()
        if len(rows) == 0:
            return None

        mangas = filter(lambda m: m.title.lower().find(manga_name.lower()) != -1, rows)
        typo_mangas = filter(lambda m: distance(manga_name.lower(), m.title.lower()) < 3, rows)
        unique_results: set[YuriManga] = set(mangas) | set(typo_mangas)

        if genres:
            unique_results = set([manga for manga in unique_results if any(g in manga.genres for g in genres)])

        if nsfw_enabled:
            return unique_results

        no_nsfw = filter(lambda m: m.get_nsfw_level() < 2 or m.nsfw == 'Suggestive', unique_results)
        return list(no_nsfw)

    except Exception as e:
        logger.error(f"Failed to retrieve data. Error: {e}")
        return None


def _map_to_yuri_mang(data, index: int) -> YuriManga | None:
    if len(data) == 0:
        return None

    desc = data[4]
    if desc == "---":
        desc = ""

    genres = str(data[5]).split(',')
    genres = [g.strip() for g in genres]

    alt_titles = {
        'jp': "",
        'en': data[4],
        'synonyms': []
    }

    return YuriManga(
        manga_id=str(index),
        source=MangaSource.SpreadSheet,
        title=data[0],
        alternative_titles=alt_titles,
        description=desc,
        nsfw_level=data[3],
        genres=genres,
        manga_format=data[7],
        publication=data[8],
        user_reading_status=data[1],
        user_score=data[2]
    )
