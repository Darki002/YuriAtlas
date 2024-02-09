from google.oauth2 import service_account
import gspread


def _get_worksheet(sheet_name):
    credentials = service_account.Credentials.from_service_account_file(
        './SpreadSheetAccess/yuriatlas-ba7416ea8160.json',
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )

    client = gspread.authorize(credentials)
    spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/10q6IqRr9kxtpZ4TKixNIEzRZXcqP_2o-mbPnt8e5vCA')
    return spreadsheet.worksheet('List')


def get_all():
    try:
        worksheet = _get_worksheet('List')
        return worksheet.get_all_values()
    except Exception as e:
        print(f"Failed to retrieve data. Error: {e}")
        return None
