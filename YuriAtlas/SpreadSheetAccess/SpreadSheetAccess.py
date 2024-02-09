import gspread
from google.oauth2 import service_account


def _get_worksheet(sheet_name):
    credentials = service_account.Credentials.from_service_account_file(
        './SpreadSheetAccess/yuriatlas-ba7416ea8160.json',
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )
    gc = gspread.authorize(credentials)

    spreadsheet = gc.open('Yuri List')
    return spreadsheet.worksheet(sheet_name)


def get_all():
    try:
        worksheet = _get_worksheet('List')
        return worksheet.get_all_values()
    except Exception as e:
        print(f"Failed to retrieve data. Error: {e}")
        return None
