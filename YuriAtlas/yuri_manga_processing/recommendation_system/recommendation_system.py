from yuri_manga_processing.preprocessing.genres.genre_processing import GenreProcessing
from yuri_manga_processing.recommendation_system.user_preferences_processor import UserPreferencesProcessor
from yuri_manga_processing.recommendation_system.yurimanga_recommendation import YuriMangaRecommendation
from yuri_manga_processing.preprocessing import mappings
from yuri_manga_processing.yuri_manga import YuriManga
from sklearn.feature_extraction.text import TfidfVectorizer
# Temp
from readinglist import user_readinglist
from readinglist.websites import Websites

MIN_SCORE = 6
COMPLETED_INDEX = mappings.COMPLETED_INDEX
PLAN_TO_READ_INDEX = mappings.PLAN_TO_READ_INDEX


def create_recommendation(user_reading_list: list[YuriManga],
                          additional_mangas: list[YuriManga],
                          genres_preprocessor: GenreProcessing) -> list[YuriManga]:

    vectorizer = TfidfVectorizer(stop_words=None)

    descriptions: list[str] = [manga.get_description() for manga in user_reading_list]
    vectorizer.fit(descriptions)

    manga_description_dict = {manga: manga.get_description() for manga in user_reading_list}
    transformed_descriptions = vectorizer.transform(list(manga_description_dict.values()))

    manga_descriptions: list[YuriMangaRecommendation] = []
    for (manga, transformed_description) in zip(manga_description_dict.keys(), transformed_descriptions):
        manga_rec = YuriMangaRecommendation(manga, transformed_description)
        manga_descriptions.append(manga_rec)

    completed_mangas = [manga for manga in manga_descriptions if manga.user_reading_status == COMPLETED_INDEX]

    completed_favorites = [manga for manga in completed_mangas if manga.user_score >= MIN_SCORE]
    plan_to_read = [manga for manga in manga_descriptions if manga.user_reading_status == PLAN_TO_READ_INDEX]

    user_preferences = UserPreferencesProcessor(completed_favorites, genres_preprocessor)
    (user_preferences
     .process_nsfw_level()
     .process_format()
     .process_genres())

    final_results: dict[YuriMangaRecommendation, float] = {}
    for manga in plan_to_read:
        result = user_preferences.compare(manga)
        # TODO: compare description
        format_weight = 0.2
        nsfw_level_weight = 0.5
        genre_weight = 0.7

        final_results[manga] = (result[0] * format_weight
                                + result[1] * nsfw_level_weight
                                + result[2] * genre_weight) / 3

    top_5 = sorted(final_results, key=final_results.get, reverse=True)[:5]
    return [manga_rec.manga for manga_rec in top_5]


if __name__ == "__main__":
    reading_list = user_readinglist.get_user_list_from("Darki002", Websites.MyAnimeList)

    print("\n")
    print("--------------------Completed Manga--------------------")
    print("\n")

    completed = [manga for manga in reading_list if manga.get_user_reading_status() == COMPLETED_INDEX]
    for c in completed:
        print(str(c))

    print("\n")
    print("--------------------Recommendation--------------------")
    print("\n")

    genre_preprocessor = GenreProcessing()
    for m in reading_list:
        m.set_genre_preprocessor(genre_preprocessor)

    recommendation = create_recommendation(reading_list, [], genre_preprocessor)

    print("\n")
    print("--------------------Best Result--------------------")
    print("\n")

    the_one = filter(lambda ma: ma.title == recommendation[0].title, reading_list)
    print(str(list(the_one)[0]))
