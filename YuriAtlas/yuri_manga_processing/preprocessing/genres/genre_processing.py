from yuri_manga_processing.preprocessing.genres.occurrence.genre_list import get_genre_list


class GenreProcessing:

    genres: dict[str, int]

    def __init__(self):
        self.genres = get_genre_list()

    @property
    def genre_count(self):
        return len(self.genres)

    def process_genre(self, genre: str) -> int | None:
        lower_genre = genre.lower()

        if lower_genre == "girls love":
            return None

        if lower_genre not in self.genres:
            self._add_and_get_number(lower_genre)
        return self.genres[lower_genre]

    def _add_and_get_number(self, genre: str) -> None:
        max_genre = max(self.genres.values())
        self.genres[genre] = max_genre + 1
