def count_names(list_of_lists, target_name):
    count = 0
    if len(list_of_lists) == 0:
        return 0
    for i in range(len(list_of_lists)):
        for j in range(len(list_of_lists[i])):
            if target_name in list_of_lists[i][j]:
                count += 1
    return count
