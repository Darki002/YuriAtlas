from data_access.yuri_manga_spreadsheet import spreadsheet_access
from yuri_manga_processing.yuri_manga import YuriManga


def learn(mangas_genres: list[list[str]], genres: list[str]) -> list[list[int]]:
    genre_count = len(genres)
    embedding = [[0 for _ in range(genre_count)] for _ in range(genre_count)]
    genres: dict[str, int] = {name: index for index, name in enumerate(genres)}

    for mg in mangas_genres:
        for i_genre in mg:
            i = genres[i_genre]
            for j_genre in mg:
                j = genres[j_genre]
                if i == j:
                    continue
                embedding[i][j] += 1
    return embedding


def main():
    all_mangas = spreadsheet_access.get_all()
    if all_mangas is None:
        print("oops")
        return

    all_genres = spreadsheet_access.get_all_genres()
    if all_genres is None:
        print("oops")
        return

    result = learn(all_mangas, all_genres)
    print(result)


if __name__ == '__main__':
    print('Start...')
    main()
