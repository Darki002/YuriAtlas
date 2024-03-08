from YuriMangaProcessing.YuriMangaProcessor import YuriManga
import requests

URL = "https://api.myanimelist.net/v2/users/{username}/mangalist"


def get_list(user_name):

    headers = {
        'X-MAL-CLIENT-ID': 'Client ID',
    }

    params = {
        'sort': 'manga_title',
        'fields': 'list_status, status, nsfw, synopsis, genres, media_type, alternative_titles',
        'limit': 100,
        'nsfw': True
    }

    response = requests.get(URL.format(username=user_name), headers=headers, params=params)

    if response.status_code == 200:
        return _map_response(response.json())
    else:
        return None


def _map_response(response):
    mangas = response["data"]

    mapped_mangas = []

    for manga in mangas:
        m = _map_manga(manga)
        mapped_mangas.append(m)

    return mapped_mangas


def _map_manga(manga_dict):

    node = manga_dict["node"]
    list_status = manga_dict["list_status"]

    genres = _get_genre_names(node["genres"])

    return YuriManga(
        title=node["title"],
        alternative_titles=node["alternative_titles"],
        description=node["synopsis"],
        nsfw_level=node["nsfw"],
        genres=genres,
        manga_format=node["media_type"],
        publication=node["status"],
        user_reading_status=list_status["status"],
        user_score=list_status["score"]
    )


def _get_genre_names(genre_list):
    genre_names = []

    for genre in genre_list:
        genre_names.append(genre["name"])

    return genre_names


if __name__ == '__main__':
    result = get_list('Darki002')
    print(result)
