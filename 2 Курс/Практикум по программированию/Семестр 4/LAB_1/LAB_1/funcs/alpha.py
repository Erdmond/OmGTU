def get_alpha(m: int) -> float:
    if m == 16:
        return 0.673
    elif m == 32:
        return 0.697
    elif m == 64:
        return 0.709
    else:
        return 0.7213 / (1 + 1.079 / m)
