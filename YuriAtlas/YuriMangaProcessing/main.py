from YuriMangaProcessing.Preprocessing.Genres.genre_processing import GenreProcessing
from ReadingList.Websites import Websites
from ReadingList.UserReadingList import get_user_list_from


def get_from_me():
    genre_processing = GenreProcessing()

    user_list = get_user_list_from("Darki002", Websites.MyAnimeList)

    if user_list is None:
        return

    [m.process(genre_processing) for m in user_list]

    print(user_list[0])


if __name__ == "__main__":
    get_from_me()
