import requests

URL = "https://api.myanimelist.net/v2/users/{username}/mangalist"


def get_list(user_name):

    headers = {
        'X-MAL-CLIENT-ID': 'Client ID',
    }

    params = {
        'sort': 'manga_title',
        'fields': 'list_status, nsfw, synopsis, genres, media_type',
        'limit': 100,
        'nsfw': 'true'
    }

    response = requests.get(URL.format(username=user_name), headers=headers, params=params)

    if response.status_code == 200:
        return _map_response(response.json())
    else:
        return None


def _map_response(response):



    return response


if __name__ == '__main__':
    result = get_list('Darki002')
    print(result)
