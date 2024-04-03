def weighted_avg(values, weights):
    if len(values) != len(weights):
        raise ValueError("Unequal lengths for values and weights")

    weighted_sum = sum(v * w for v, w in zip(values, weights))
    return weighted_sum / sum(weights)


def exponential_decay(x, base=0.8, exponent=-1):
    if base <= 0 or base >= 1:
        raise ValueError("Base must be between 0 and 1")
    return base**(exponent * x)
