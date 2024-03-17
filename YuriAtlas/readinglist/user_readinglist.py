from yuri_manga_processing.yuri_manga import YuriManga
from .my_anime_list import get_list
from .websites import Websites


def get_user_list_from(user_name: str, website: Websites | None) -> list[YuriManga] | None:
    if website == Websites.MyAnimeList:
        return get_list(user_name)
    else:
        return None
