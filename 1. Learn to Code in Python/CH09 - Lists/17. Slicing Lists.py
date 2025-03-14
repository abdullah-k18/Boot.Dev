def get_champion_slices(champions):
    first = champions[2:]
    second = champions[:-1]
    third = champions[::2]

    return first, second, third

