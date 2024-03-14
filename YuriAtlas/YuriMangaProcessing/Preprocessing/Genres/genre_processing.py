import genre_list


class GenreProcessing:

    genres: dict[str, int]

    def __init__(self):
        self.genres = genre_list.get()

    def process_genre(self, genre: str) -> int:
        if genre not in self.genres:
            self._try_add_and_get_number(genre)
        return self.genres[genre]

    def _try_add_and_get_number(self, genre: str) -> None:
        if genre not in self.genres:
            max_genre = max(self.genres.values())
            self.genres[genre] = max_genre + 1
