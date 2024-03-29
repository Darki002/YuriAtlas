from yuri_manga_processing.preprocessing.genres.genre_processing import GenreProcessing
from yuri_manga_processing.recommendation_system.yurimanga_recommendation import YuriMangaRecommendation


class UserPreferencesProcessor:
    def __init__(self, user_favorites: list[YuriMangaRecommendation], genrs_processor: GenreProcessing):
        self.user_favorites: list[YuriMangaRecommendation] = user_favorites
        self.genrs_processor: GenreProcessing = genrs_processor
        self.processed_nsfw_levels: dict[int, int] | None = None
        self.processed_format: dict[int, int] | None = None
        self.processed_genres: dict[int, int] | None = None

    # NSFW Level
    def process_nsfw_level(self):
        nsfw_counts: dict[int, int] = {}
        for manga in self.user_favorites:
            nsfw_counts[manga.nsfw_level] = nsfw_counts.get(manga.nsfw_level, 0) + 1

        self.processed_nsfw_levels = nsfw_counts
        return self

    def get_nsfw_level(self) -> dict[int, int]:
        if self.processed_nsfw_levels is None:
            self.process_nsfw_level()
        return self.processed_nsfw_levels

    def compare_nsfw_level(self, manga: YuriMangaRecommendation) -> float:
        if self.processed_nsfw_levels is None:
            raise ValueError("NSFW Levels have not been processed")

        manga_nsfw_level_count = self.processed_nsfw_levels.get(manga.manga_format, 0)
        max_nsfw_level_count = max(self.processed_nsfw_levels.values())
        return manga_nsfw_level_count / max_nsfw_level_count

    # Format
    def process_format(self):
        format_counts: dict[int, int] = {}
        for manga in self.user_favorites:
            format_counts[manga.manga_format] = format_counts.get(manga.manga_format, 0) + 1

        self.processed_format = format_counts
        return self

    def get_format(self) -> dict[int, int]:
        if self.processed_format is None:
            self.process_format()
        return self.processed_format

    def compare_format(self, manga: YuriMangaRecommendation) -> float:
        if self.processed_format is None:
            raise ValueError("Format has not been processed")

        manga_format_count = self.processed_format.get(manga.manga_format, 0)
        max_format_count = max(self.processed_format.values())
        return manga_format_count / max_format_count

    # Genres
    def process_genres(self):
        genres_counts: dict[int, int] = {}
        for manga in self.user_favorites:
            for genre in manga.genres:
                genres_counts[genre] = genres_counts.get(genre, 0) + 1

        self.processed_genres = genres_counts
        return self

    def get_genres(self) -> dict[int, int]:
        if self.processed_genres is None:
            self.process_genres()
        return self.processed_genres

    def compare_genres(self, manga: YuriMangaRecommendation) -> float:
        if self.processed_genres is None:
            raise ValueError("Genres have not been processed")

        matches: int = 0

        for genre in manga.genres:
            if genre in self.processed_genres.keys():
                matches += 1

        return matches / self.genrs_processor.genre_count

    # Helper
    def compare(self, manga: YuriMangaRecommendation) -> tuple[float, float, float]:
        format_result = self.compare_format(manga)
        nsfw_level_result = self.compare_nsfw_level(manga)
        genres_result = self.compare_genres(manga)

        return format_result, nsfw_level_result, genres_result
