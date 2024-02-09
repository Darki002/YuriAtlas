from YuriMangaListAccess.YuriManga import YuriManga
from google.oauth2 import service_account
import gspread
import logging


def _get_worksheet(worksheet_id):
    credentials = service_account.Credentials.from_service_account_file(
        './YuriMangaListAccess/yuriatlas-ba7416ea8160.json',
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )

    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_key('10q6IqRr9kxtpZ4TKixNIEzRZXcqP_2o-mbPnt8e5vCA')
    return spreadsheet.get_worksheet_by_id(worksheet_id)


def get_all():
    try:
        worksheet = _get_worksheet(0)
        rows = worksheet.get_all_values()
        return [YuriManga.from_row(row) for row in rows]
    except Exception as e:
        logging.error(f"Failed to retrieve data. Error: {e}")
        return None
