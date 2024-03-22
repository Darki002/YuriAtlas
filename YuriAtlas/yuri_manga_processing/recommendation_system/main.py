from yuri_manga_processing.recommendation_system.user_preferences_processor import UserPreferencesProcessor
from yuri_manga_processing.recommendation_system.yurimanga_recommendation import YuriMangaRecommendation
from yuri_manga_processing.preprocessing import mappings
from yuri_manga_processing.yuri_manga import YuriManga
from sklearn.feature_extraction.text import TfidfVectorizer

MIN_SCORE = 6
COMPLETED_INDEX = mappings.COMPLETED_INDEX
PLAN_TO_READ_INDEX = mappings.PLAN_TO_READ_INDEX


def create_recommendation(user_reading_list: list[YuriManga], spreadsheet: list[YuriManga]) -> list[YuriManga]:
    vectorizer = TfidfVectorizer()

    completed_mangas = [manga for manga in user_reading_list if manga.get_user_reading_status() == COMPLETED_INDEX]

    for manga in user_reading_list:
        description = manga.get_description()
        vectorizer.fit(description)

    manga_descriptions: list[YuriMangaRecommendation] = []

    for index, manga in enumerate(user_reading_list):
        transformed_description = vectorizer.transform(manga.get_description())
        manga_rec = YuriMangaRecommendation(index, manga, transformed_description)
        manga_descriptions.append(manga_rec)

    completed_mangas = [manga for manga in manga_descriptions if manga.user_reading_status == COMPLETED_INDEX]

    completed_favorites = [manga for manga in completed_mangas if manga.user_score >= MIN_SCORE]
    plan_to_read = [manga for manga in manga_descriptions if manga.user_reading_status == PLAN_TO_READ_INDEX]

    user_preferences = UserPreferencesProcessor(completed_favorites)

    nsfw_counts: dict[int, int] = user_preferences.get_nsfw_level()
    format_counts: dict[int, int] = user_preferences.get_format()

    # TODO: Compare the mangas from the favorites and the plan_to_read
    # TODO: make ranking of the best matches

    return []


def compare_genres(manga1_genres: list[int], manga2_genres: list[int]) -> int:
    shared_genres = set(manga1_genres).intersection(set(manga2_genres))
    return len(shared_genres)
