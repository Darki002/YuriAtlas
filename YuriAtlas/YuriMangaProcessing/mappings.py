def from_manga_format_to_numeric(manga_format):
    match manga_format:
        case 'unknown':
            return 0
        case 'manga':
            return 1
        case 'novel':
            return 2
        case 'one_shot':
            return 3
        case 'doujinshi':
            return 4
        case 'manhwa':
            return 5
        case 'manhua':
            return 6
        case 'oel':
            return 7
        case _:
            return 0


def from_nsfw_level_to_numeric(nsfw_level):
    match nsfw_level:
        case 'no' | 'white':
            return 0
        case 'Suggestive' | 'gray':
            return 1
        case 'Erotic' | 'NSFW' | 'black':
            return 2
        case _:
            return 0
