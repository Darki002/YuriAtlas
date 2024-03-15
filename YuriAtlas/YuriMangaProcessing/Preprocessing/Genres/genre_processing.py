from genre_list import get_genre_list


class GenreProcessing:

    genres: dict[str, int]

    def __init__(self):
        self.genres = get_genre_list()

    def process_genre(self, genre: str) -> int:
        lower_genre = genre.lower()

        if lower_genre not in self.genres:
            self._try_add_and_get_number(lower_genre)
        return self.genres[lower_genre]

    def _try_add_and_get_number(self, genre: str) -> None:
        if genre not in self.genres:
            max_genre = max(self.genres.values())
            self.genres[genre] = max_genre + 1
