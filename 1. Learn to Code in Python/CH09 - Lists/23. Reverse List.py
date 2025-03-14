def reverse_array(items):
    reversed = []

    for i in range(len(items)):
        rev = items.pop()
        reversed.append(rev)
    return reversed

