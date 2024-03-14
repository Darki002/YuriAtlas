from YuriMangaProcessing.Preprocessing.text_preprocessing import TextPreprocessor
from YuriMangaProcessing.Preprocessing import mappings


class YuriManga:
    def __init__(self, title: str, alternative_titles: dict[str] | None, description: str, nsfw_level: str,
                 genres: list[str], manga_format: str, publication: str, user_reading_status: str, user_score: int):
        self.title: str = title
        self.alternative_titles: dict[str] | None = alternative_titles
        self.description: str = description
        self.nsfw_level: str = nsfw_level
        self.genres: list[str] = genres
        self.manga_format: str = manga_format
        self.publication: str = publication
        self.user_reading_status: str = user_reading_status
        self.user_score: int = user_score
        # Processed data
        self._processed_description: list[str] | None = None
        self._processed_nsfw_level: int | None = None
        self._processed_genres: list[int] | None = None
        self._processed_publication: int | None = None
        self._processed_manga_format: int | None = None
        self._processed_user_reading_status: int | None = None

    # Description
    def process_description(self):
        preprocessor = TextPreprocessor(self.description)
        self._processed_description = preprocessor.process().text

    def get_description(self):
        if self._processed_description is None:
            self.process_description()
        return self._processed_description

    # NSFW Level
    def process_nsfw_level(self):
        self._processed_nsfw_level = mappings.from_nsfw_level_to_numeric(self.nsfw_level)

    def get_nsfw_level(self) -> int:
        if self._processed_nsfw_level is None:
            self.process_nsfw_level()
        return self._processed_nsfw_level

    # Genres
    def process_genres(self):
        self._processed_genres = self.genres  # TODO Processing

    def get_genres(self) -> list[int]:
        if self._processed_genres is None:
            self.process_genres()
        return self._processed_genres

    # Manga Format
    def process_manga_format(self):
        self._processed_manga_format = mappings.from_manga_format_to_numeric(self.manga_format)

    def get_manga_format(self) -> int:
        if self._processed_manga_format is None:
            self.process_manga_format()
        return self._processed_manga_format

    # Publication
    def process_publication(self):
        self._processed_publication = mappings.from_publication_to_numeric(self.publication)

    def get_publication(self) -> int:
        if self._processed_publication is None:
            self.process_publication()
        return self._processed_publication

    # User Reading Status
    def process_user_reading_status(self):
        self._processed_user_reading_status = mappings.from_user_reading_status_to_numeric(self.user_reading_status)

    def get_user_reading_status(self) -> int:
        if self._processed_user_reading_status is None:
            self.process_user_reading_status()
        return self._processed_user_reading_status

    # User Score
    def get_user_score(self) -> int:
        return self.user_score

    # Alternative Title
    def get_alternative_title_en(self):
        return self.alternative_titles['en']

    def get_alternative_title_ja(self):
        return self.alternative_titles['ja']

    def get_alternative_title_synonyms(self):
        return self.alternative_titles['synonyms']
