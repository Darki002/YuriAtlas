from data_access.yuri_manga_spreadsheet import spreadsheet_access
from yuri_manga_processing.yuri_manga import YuriManga


def learn(mangas: list[YuriManga], genres: list[str]):
    genre_count = len(genres)
    embedding = [[0 for _ in range(genre_count)] for _ in range(genre_count)]
    genres: dict[str, int] = {name: index for index, name in enumerate(genres)}

    for i_manga in mangas:
        for j_manga in mangas:
            if j_manga == i_manga:
                continue


if __name__ is '__main__':
    print('Start...')
    all_mangas = spreadsheet_access.get_all()
    all_genres = spreadsheet_access.get_all_genres()
    learn(all_mangas, all_genres)
