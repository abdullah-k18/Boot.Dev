def get_odds_and_evens(numbers):
    num_odds = 0
    num_evens = 0

    # Don't touch above this line

    for i in range(len(numbers)):
        if (numbers[i] % 2) == 0:
            num_evens += 1
        else:
            num_odds += 1
    return num_odds, num_evens
