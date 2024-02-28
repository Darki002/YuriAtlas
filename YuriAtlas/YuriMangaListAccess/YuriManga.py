from DescriptionProcessing.preprocessing import TextPreprocessor


class YuriManga:
    def __init__(self, title, alternative_title, description, nsfw_level, genres, manga_format, publication):
        self.title = title
        self.alternative_title = alternative_title
        self.description = description
        self.nsfw_level = nsfw_level
        self.genres = genres
        self.manga_format = manga_format
        self.publication = publication
        # Processed data
        self._processed_description = None
        self._processed_nsfw_level = None

    def process_nsfw_level(self):
        match self.nsfw_level:
            case 'No':
                self._processed_nsfw_level = 0
            case 'Suggestive':
                self._processed_nsfw_level = 1
            case 'Erotic' | 'NSFW':
                self._processed_nsfw_level = 2
            case _:
                self._processed_nsfw_level = 0

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
