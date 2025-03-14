def sum_nested_list(lst):
    size = 0
    for i in lst:
        if isinstance(i, int):
            size += i
        elif isinstance(i, list):
            size += (sum_nested_list(i))
    return size

