import MyAnimeList
from Websites import Websites


def get_user_list_from(user_name, website):
    if website == Websites.MyAnimeList:
        return MyAnimeList.get_list(user_name)
