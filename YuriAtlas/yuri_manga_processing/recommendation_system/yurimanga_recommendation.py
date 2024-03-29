from yuri_manga_processing.yuri_manga import YuriManga


class YuriMangaRecommendation:
    def __init__(self, manga_id: int, manga: YuriManga, transformed_description):
        self.manga_id: int = manga_id
        self.manga: YuriManga = manga
        self.transformed_description = transformed_description

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

    def compare_genres(self, other: 'YuriMangaRecommendation', total_genre_count) -> float:
        shared_genres = set(self.genres).intersection(set(other.genres))
        return len(shared_genres) / total_genre_count
