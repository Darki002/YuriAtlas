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
        self._title = title
        self._alternative_title = alternative_title
        self._nsfw = nsfw
        self._genres = genres
        self._manga_format = manga_format
        self._publication = publication
        self._link = link

    @property
    def title(self):
        return self._title

    @property
    def alternative_title(self):
        return self._alternative_title

    @property
    def nsfw(self):
        return self._nsfw

    @property
    def genres(self):
        return self._genres

    @property
    def manga_format(self):
        return self._manga_format

    @property
    def publication(self):
        return self._publication

    @property
    def link(self):
        return self._link

    @classmethod
    def from_row(cls, row):

        if len(row) == 0:
            return None

        genres = str(row[5]).split(',')
        genres = [g.strip() for g in genres]

        return cls(
            title=row[0],
            alternative_title=row[4],
            nsfw=row[3],
            genres=genres,
            manga_format=row[6],
            publication=row[7],
            link=row[8]
        )
