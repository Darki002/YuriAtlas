class YuriManga:
    def __init__(
            self,
            title,
            alternative_title,
            nsfw,
            genres,
            manga_format,
            publication,
            link):
        self.title = title
        self.alternative_title = alternative_title
        self.nsfw = nsfw
        self.genres = genres
        self.manga_format = manga_format
        self.publication = publication
        self.link = link

    @classmethod
    def from_row(cls, row):
        return cls(
            title=row[0],
            alternative_title=row[4],
            nsfw=row[3],
            genres=row[5],
            manga_format=row[6],
            publication=row[7],
            link=row[8]
        )
