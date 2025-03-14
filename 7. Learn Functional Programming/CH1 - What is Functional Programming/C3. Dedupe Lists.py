def deduplicate_lists(lst1, lst2, reverse=False):
    set1 = set()
    list1 = []
    for elem in lst1:
        set1.add(elem)
    for elem in lst2:
        set1.add(elem)
    for elem in set1:
        list1.append(elem)
    return sorted(list1, reverse=reverse)

