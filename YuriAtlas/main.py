import SpreadSheetAccess.SpreadSheetAccess as Ssa


def main():
    rows = Ssa.get_all()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
