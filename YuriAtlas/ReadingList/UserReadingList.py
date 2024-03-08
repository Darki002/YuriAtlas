import MyAnimeList


def get_user_list_from(user_name, website):
    # TODO check domain, which website is it from
    # Example Link: https://myanimelist.net/mangalist/Darki002
    if website == "MyAnimeList":
        return MyAnimeList.get_list(user_name)


if __name__ == '__main__':
    result = get_user_list_from('Darki002', 'MyAnimeList')
    print(result)
