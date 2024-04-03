from yuri_manga_processing.yuri_manga import YuriManga
from data_access.api_access.my_anime_list import get_list
from data_access.api_access.apisource import ApiSource


def get_user_list_from(user_name: str, source: ApiSource | None) -> list[YuriManga] | None:
    if source == ApiSource.MyAnimeList:
        return get_list(user_name)
    else:
        return None
