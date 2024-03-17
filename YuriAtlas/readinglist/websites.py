import enum


class Websites(enum.Enum):
    MyAnimeList = "MyAnimeList"

    @classmethod
    def try_from(cls, string: str):
        if string == cls.MyAnimeList:
            return cls.MyAnimeList
        return None
