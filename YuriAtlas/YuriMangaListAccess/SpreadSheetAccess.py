from YuriManga.YuriMangaLegacy import YuriMangaLegacy
from YuriMangaListAccess.LevensteinsDistance import distance
from google.oauth2 import service_account
import gspread
import logging


def _get_worksheet(worksheet_index):
    credentials = service_account.Credentials.from_service_account_file(
        './YuriMangaListAccess/yuriatlas-ba7416ea8160.json',
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )

    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_key('10q6IqRr9kxtpZ4TKixNIEzRZXcqP_2o-mbPnt8e5vCA')
    return spreadsheet.get_worksheet(worksheet_index)


def get_all_genres():
    worksheet = _get_worksheet(2)
    genres = worksheet.col_values(19)
    return genres


def get_all():
    try:
        worksheet = _get_worksheet(1)
        rows = worksheet.get_all_values()
        return [YuriMangaLegacy.from_row(row) for row in rows]

    except Exception as e:
        logging.error(f"Failed to retrieve data. Error: {e}")
        return None


def get_by_name(manga_name):
    try:
        rows = get_all()
        if len(rows) == 0:
            return None

        mangas = filter(lambda m: m.title == manga_name, rows)
        return next(mangas, None)

    except Exception as e:
        logging.error(f"Failed to retrieve data. Error: {e}")
        return None


def search_by_name(manga_name, nsfw_enabled):
    try:
        rows = get_all()
        if len(rows) == 0:
            return None

        mangas = filter(lambda m: m.title.lower().find(manga_name.lower()) != -1, rows)
        typo_mangas = filter(lambda m: distance(manga_name.lower(), m.title.lower()) < 3, rows)
        unique_results = set(mangas) | set(typo_mangas)

        if nsfw_enabled:
            return list(unique_results)

        no_nsfw = filter(lambda m: m.nsfw == 'No' or m.nsfw == 'Suggestive', unique_results)
        return list(no_nsfw)

    except Exception as e:
        logging.error(f"Failed to retrieve data. Error: {e}")
        return None
