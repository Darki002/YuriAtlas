from sklearn.metrics.pairwise import cosine_similarity
from yuri_manga_processing.yuri_manga import YuriManga


class YuriMangaRecommendation:
    def __init__(self, manga: YuriManga):
        self.manga: YuriManga = manga
        self.tfidf_description = None

    @property
    def genres(self) -> list[int]:
        return self.manga.get_genres()

    @property
    def nsfw_level(self) -> int:
        return self.manga.get_nsfw_level()

    @property
    def manga_format(self) -> int:
        return self.manga.get_manga_format()

    @property
    def user_reading_status(self) -> int:
        return self.manga.get_user_reading_status()

    @property
    def user_score(self) -> int:
        return self.manga.get_user_score()

    @property
    def description(self) -> str:
        return self.manga.get_description()

    def set_tfdtf_description(self, tfdtf_description):
        self.tfidf_description = tfdtf_description

    def compare_description(self, other: 'YuriMangaRecommendation'):
        return cosine_similarity(self.description, other.description)
