def exponential_growth(n, factor, days):
    arr = []
    arr.append(n)
    for i in range(days):
        n2 = n * factor
        n = n2
        arr.append(n2)
    return arr
