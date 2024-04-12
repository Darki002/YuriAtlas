class GenreEmbedding:
    embedding: dict[str, list[int]] | None = None

    def load(self):
        self.embedding = None  # TODO: Load the saved embedding

    def transform(self, genre: str) -> list[int]:
        vec = self.embedding.get(genre)
        if vec is None:
            raise ValueError("Can not transform unknown genre")
        return vec
