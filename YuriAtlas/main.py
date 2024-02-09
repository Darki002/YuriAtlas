from YuriMangaListAccess import SpreadSheetAccess as Ssa


def main():
    rows = Ssa.get_all()

    if rows is not None:
        print(len(rows))


if __name__ == '__main__':
    main()
