from YuriMangaListAccess import SpreadSheetAccess


def main():
    rows = SpreadSheetAccess.get_all()

    if rows is not None:
        c = rows[0]
        print(c.title)
        print(c.alternative_title)
        print(c.nsfw)
        print(c.genres)
        print(c.manga_format)
        print(c.publication)
        print(c.link)

    print('-------------')

    cp = SpreadSheetAccess.get_by_name('Citrus+')
    print(cp.title)


if __name__ == '__main__':
    main()
