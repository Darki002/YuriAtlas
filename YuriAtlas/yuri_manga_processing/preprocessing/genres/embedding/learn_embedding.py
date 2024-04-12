from data_access.yuri_manga_spreadsheet import spreadsheet_access
from timeit import default_timer as timer


def learn(mangas_genres: list[list[str]], genres: list[str]) -> dict[str, list[int]]:
    genre_count = len(genres)
    matrix = [[0 for _ in range(genre_count)] for _ in range(genre_count)]
    genres: dict[str, int] = {name: index for index, name in enumerate(genres)}

    for mg in mangas_genres:
        for i_genre in mg:
            i = genres[i_genre]
            for j_genre in mg:
                j = genres[j_genre]
                if i == j:
                    continue
                matrix[i][j] += 1

    print(matrix)

    embedding: dict[str, list[int]] = {}
    for genre, vec in zip(genres, matrix):
        embedding[genre] = vec
    return embedding


def get_data():
    all_mangas = spreadsheet_access.get_all()
    if all_mangas is None:
        print("oops")
        return
    all_genres = spreadsheet_access.get_all_genres()
    if all_genres is None:
        print("oops")
        return
    return all_mangas, all_genres


def main():
    y1 = ["Fantasy", "Action", "Comedy"]
    y2 = ["Comedy", "School Life", "Romance"]
    y3 = ["Romance", "Drama", "Fantasy", "Action"]
    genres = ["Fantasy", "Action", "Comedy", "School Life", "Romance", "Drama"]

    result = learn([y1, y2, y3], genres)
    print(result)

    # TODO: Create Embedding and save it as a file


if __name__ == '__main__':
    print('Start...')
    start = timer()
    main()
    end = timer()
    print(f"Duration: {end - start}")
