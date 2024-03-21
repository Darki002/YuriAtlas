from yuri_manga_processing.yuri_manga import YuriManga


class YuriMangaRecommendation:
    def __init__(self, manga_id: int, manga: YuriManga, transformed_description):
        self.manga_id: int = manga_id
        self.manga: YuriManga = manga
        self.transformed_description = transformed_description
