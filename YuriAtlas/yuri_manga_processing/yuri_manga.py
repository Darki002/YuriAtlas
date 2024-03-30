from .manga_source import MangaSource
from .preprocessing.description.text_preprocessing import TextPreprocessor
from .preprocessing.genres.genre_processing import GenreProcessing
from .preprocessing import mappings


class YuriManga:
    genre_preprocessor: GenreProcessing | None = None

    def __init__(self, manga_id: str, source: MangaSource, title: str, alternative_titles: dict[str, any] | None, description: str,
                 nsfw_level: str, genres: list[str], manga_format: str, publication: str, user_reading_status: str,
                 user_score: int | None):
        self.manga_id: str = manga_id
        self.source: MangaSource = source
        self.title: str = title
        self.alternative_titles: dict[str, any] | None = alternative_titles
        self.description: str = description
        self.nsfw_level: str = nsfw_level
        self.genres: list[str] = genres
        self.manga_format: str = manga_format
        self.publication: str = publication
        self.user_reading_status: str = user_reading_status
        self.user_score: int | None = user_score
        # Processed data
        self._processed_description: list[str] | None = None
        self._processed_nsfw_level: int | None = None
        self._processed_genres: list[int] | None = None
        self._processed_publication: int | None = None
        self._processed_manga_format: int | None = None
        self._processed_user_reading_status: int | None = None

    def set_genre_preprocessor(self, genre_preprocessor: GenreProcessing):
        self.genre_preprocessor = genre_preprocessor
        return self

    # Description
    def process_description(self):
        preprocessor = TextPreprocessor(self.description)
        self._processed_description = preprocessor.process().text
        return self

    def get_description(self) -> str:
        if self._processed_description is None:
            self.process_description()
        return ' '.join(self._processed_description)

    # NSFW Level
    def process_nsfw_level(self):
        self._processed_nsfw_level = mappings.from_nsfw_level_to_numeric(self.nsfw_level)
        return self

    def get_nsfw_level(self) -> int:
        if self._processed_nsfw_level is None:
            self.process_nsfw_level()
        return self._processed_nsfw_level

    # Genres
    def process_genres(self):
        if self.genre_preprocessor is None:
            raise ValueError("No genre preprocessor defined")
        self._processed_genres = [self.genre_preprocessor.process_genre(genre) for genre in self.genres]
        self._processed_genres = [genre for genre in self._processed_genres if genre is not None]
        return self

    def get_genres(self) -> list[int]:
        if self._processed_genres is None:
            self.process_genres()
        return self._processed_genres

    # Manga Format
    def process_manga_format(self):
        self._processed_manga_format = mappings.from_manga_format_to_numeric(self.manga_format)
        return self

    def get_manga_format(self) -> int:
        if self._processed_manga_format is None:
            self.process_manga_format()
        return self._processed_manga_format

    # Publication
    def process_publication(self):
        self._processed_publication = mappings.from_publication_to_numeric(self.publication)
        return self

    def get_publication(self) -> int:
        if self._processed_publication is None:
            self.process_publication()
        return self._processed_publication

    # User Reading Status
    def process_user_reading_status(self):
        self._processed_user_reading_status = mappings.from_user_reading_status_to_numeric(self.user_reading_status)
        return self

    def get_user_reading_status(self) -> int:
        if self._processed_user_reading_status is None:
            self.process_user_reading_status()
        return self._processed_user_reading_status

    # User Score
    def get_user_score(self) -> int:
        return self.user_score

    # Alternative Title
    def has_english_title(self) -> bool:
        return "en" in self.alternative_titles.keys() and self.alternative_titles["en"]

    def get_alternative_title_en(self) -> str:
        return self.alternative_titles['en']

    def get_alternative_title_ja(self) -> str:
        return self.alternative_titles['ja']

    def get_alternative_title_synonyms(self) -> list[str]:
        return self.alternative_titles['synonyms']

    def process(self, genre_preprocessor: GenreProcessing):
        self.genre_preprocessor = genre_preprocessor
        (self.process_description()
         .process_nsfw_level()
         .process_genres()
         .process_manga_format()
         .process_publication()
         .process_user_reading_status())
        return self

    def __str__(self) -> str:
        result = (f'Title: {self.title} \n'
                  f'Alternative Titles: {self.alternative_titles} \n'
                  f'Description: {self.description} \n'
                  f'NSFW Level: {self.nsfw_level} \n'
                  f'Manga Format: {self.manga_format} \n'
                  f'Publication: {self.publication} \n'
                  f'User Reading Status: {self.user_reading_status} \n'
                  f'User Score: {self.user_score} \n')

        result = f'{result} Genres: {self.genres} \n'

        if self._processed_description is not None:
            result += f'Processed Description: {self._processed_description} \n'

        if self._processed_nsfw_level is not None:
            result += f'Processed NSFW Level: {self._processed_nsfw_level} \n'

        if self._processed_manga_format is not None:
            result += f'Processed Manga Format: {self._processed_manga_format} \n'

        if self._processed_publication is not None:
            result += f'Processed Publication: {self._processed_publication} \n'

        if self._processed_user_reading_status is not None:
            result += f'Processed User Reading Status: {self._processed_user_reading_status} \n'

        if self._processed_genres is not None:
            result += f'Processed Genres: {self._processed_genres} \n'

        return result
