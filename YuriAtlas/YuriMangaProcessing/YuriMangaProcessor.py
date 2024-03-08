from YuriMangaProcessing.DescriptionProcessing.preprocessing import TextPreprocessor
import mappings


class YuriManga:
    def __init__(self, title, alternative_titles, description, nsfw_level, genres, manga_format, publication,
                 user_reading_status, user_score):
        self.title = title
        self.alternative_titles = alternative_titles
        self.description = description
        self.nsfw_level = nsfw_level
        self.genres = genres
        self.manga_format = manga_format
        self.publication = publication
        self.user_reading_status = user_reading_status
        self.user_score = user_score
        # Processed data
        self._processed_description = None
        self._processed_nsfw_level = None
        self._processed_manga_format = None

    def process_nsfw_level(self):
        self._processed_nsfw_level = mappings.from_nsfw_level_to_numeric(self.nsfw_level)

    def get_processed_nsfw_level(self):
        if self._processed_nsfw_level is None:
            self.process_nsfw_level()
        return self._processed_nsfw_level

    def process_description(self):
        preprocessor = TextPreprocessor(self.description)
        self._processed_description = preprocessor.process().text

    def get_processed_description(self):
        if self._processed_description is None:
            self.process_description()
        return self._processed_description

    def process_manga_format(self):
        self._processed_manga_format = mappings.from_manga_format_to_numeric(self.manga_format)

    def get_processed_manga_format(self):
        if self._processed_manga_format is None:
            self.process_manga_format()
        return self._processed_manga_format

    def get_alternative_title_en(self):
        return self.alternative_titles['en']

    def get_alternative_title_ja(self):
        return self.alternative_titles['ja']

    def get_alternative_title_synonyms(self):
        return self.alternative_titles['synonyms']
