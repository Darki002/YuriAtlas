from yuri_manga_processing.preprocessing.genres.genre_processing import GenreProcessing
from yuri_manga_processing.recommendation_system.user_preferences_processor import UserPreferencesProcessor
from yuri_manga_processing.recommendation_system.yurimanga_recommendation import YuriMangaRecommendation
from yuri_manga_processing.recommendation_system.rec_weights import RecWeights
from yuri_manga_processing.preprocessing import mappings
from yuri_manga_processing.yuri_manga import YuriManga
from sklearn.feature_extraction.text import TfidfVectorizer
from math_helper.lin_algebra import cosine_sim
from math_helper.avg import weighted_avg, exponential_decay


class RecommendationEngine:
    min_score = 6
    completed_index = mappings.COMPLETED_INDEX
    plan_to_read_index = mappings.PLAN_TO_READ_INDEX

    plan_to_read: list[YuriMangaRecommendation] | None = None
    favorites: list[YuriMangaRecommendation] | None = None

    vectorizer = TfidfVectorizer(stop_words=None)
    genres_preprocessor: GenreProcessing = GenreProcessing()
    user_preferences: UserPreferencesProcessor | None = None
    rec_weights: RecWeights = RecWeights()

    def __init__(self, mangas: list[YuriManga], additional_mangas: list[YuriManga] = ()):
        self.mangas: list[YuriMangaRecommendation] = [YuriMangaRecommendation(m) for m in mangas]
        self.additional_mangas: list[YuriMangaRecommendation] = [YuriMangaRecommendation(a) for a in additional_mangas]

    def set_up(self):
        for manga in self.mangas + self.additional_mangas:
            manga.manga.set_genre_preprocessor(self.genres_preprocessor)

        completed_mangas = [manga for manga in self.mangas if manga.user_reading_status == self.completed_index]
        self.favorites = [manga for manga in completed_mangas if manga.user_score >= self.min_score]
        self.plan_to_read = [manga for manga in self.mangas if manga.user_reading_status == self.plan_to_read_index]

        self.user_preferences = UserPreferencesProcessor(self.favorites, self.genres_preprocessor)

    def create_recommendation(self) -> list[YuriManga]:

        if self.user_preferences is None or self.plan_to_read is None or self.favorites is None:
            raise ValueError("Not properly set up. Probably set_up() wasn't called.")

        self._fit()._transform()

        final_results: dict[YuriMangaRecommendation, float] = {}
        for manga in self.plan_to_read:
            result = self.user_preferences.compare(manga)

            similarities = [cosine_sim(fav.tfdtf_description, manga.tfdtf_description) for fav in self.favorites]

            similarities = sorted(similarities, reverse=True)
            weights = [exponential_decay(i) for i in similarities]

            dec_sim = weighted_avg(similarities, weights)

            final_values = [*result, dec_sim]
            final_results[manga] = weighted_avg(final_values, self.rec_weights.weights)

        top_5 = sorted(final_results, key=final_results.get, reverse=True)[:5]
        return [manga_rec.manga for manga_rec in top_5]

    def _fit(self):
        all_mangas = self.mangas + self.additional_mangas
        descriptions: list[str] = [manga.description for manga in all_mangas]
        self.vectorizer.fit(descriptions)

        (self.user_preferences
         .process_nsfw_level()
         .process_format()
         .process_genres())
        return self

    def _transform(self):
        manga_description_dict = {manga: manga.description for manga in self.mangas}
        transformed_descriptions = self.vectorizer.transform(list(manga_description_dict.values()))

        for (manga, transformed_description) in zip(manga_description_dict.keys(), transformed_descriptions):
            manga.set_tfdtf_description(transformed_description)
        return self
