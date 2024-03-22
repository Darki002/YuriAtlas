from yuri_manga_processing.recommendation_system.yurimanga_recommendation import YuriMangaRecommendation


class UserPreferencesProcessor:
    def __init__(self, user_favorites: list[YuriMangaRecommendation]):
        self.user_favorites = user_favorites
        self.processed_nsfw_levels: dict[int, int] | None = None
        self.processed_format: dict[int, int] | None = None

    # NSFW Level
    def process_nsfw_level(self):
        nsfw_counts: dict[int, int] = {}
        for manga in self.user_favorites:
            nsfw_counts[manga.nsfw_level] += 1

        self.processed_nsfw_levels = nsfw_counts

    def get_nsfw_level(self) -> dict[int, int]:
        if self.processed_nsfw_levels is None:
            self.process_nsfw_level()
        return self.processed_nsfw_levels

    # Format
    def process_format(self):
        format_counts: dict[int, int] = {}
        for manga in self.user_favorites:
            format_counts[manga.manga_format] += 1

        self.processed_format = format_counts

    def get_format(self) -> dict[int, int]:
        if self.processed_format is None:
            self.process_format()
        return self.processed_format
