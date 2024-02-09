from YuriMangaListAccess import SpreadSheetAccess


def main():
    rows = SpreadSheetAccess.get_all()

    if rows is not None:
        print(len(rows))


if __name__ == '__main__':
    main()
