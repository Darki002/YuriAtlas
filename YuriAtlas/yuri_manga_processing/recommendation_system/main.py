from yuri_manga_processing.yuri_manga import YuriManga
from sklearn.feature_extraction.text import TfidfVectorizer

MIN_SCORE = 6
COMPLETED_INDEX = 1
PLAN_TO_READ_INDEX = 4


def create_recommendation(user_reading_list: list[YuriManga], spreadsheet: list[YuriManga]) -> list[YuriManga]:
    completed_mangas = [manga for manga in user_reading_list if manga.get_user_reading_status() == COMPLETED_INDEX]
    plan_to_read = [manga for manga in user_reading_list if manga.get_user_reading_status() == PLAN_TO_READ_INDEX]

    completed_favorites = [manga for manga in completed_mangas if manga.user_score >= MIN_SCORE]

    return []
