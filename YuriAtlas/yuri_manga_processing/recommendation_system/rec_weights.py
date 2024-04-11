class RecWeights:
    default_format_weight: float = 0.1
    default_nsfw_level_weight: float = 0.3
    default_genre_weight: float = 0.8
    default_description_weight: float = 0.5

    weights: list[float] = \
        [default_format_weight, default_nsfw_level_weight, default_genre_weight, default_description_weight]

    def __init__(self, format_weight: float | None = None,
                 nsfw_level_weight: float | None = None,
                 genre_weight: float | None = None,
                 description_weight: float | None = None):
        if format_weight is not None:
            self.weights[0] = format_weight
        if nsfw_level_weight is not None:
            self.weights[1] = nsfw_level_weight
        if genre_weight is not None:
            self.weights[2] = genre_weight
        if description_weight is not None:
            self.weights[3] = description_weight
