def find_missing_ids(first_ids, second_ids):
    first_id = set()
    second_id = set()
    diff = []
    for id in first_ids:
        first_id.add(id)
    for id in second_ids:
        second_id.add(id)

    difference = first_id.difference(second_id)
    for i in difference:
        diff.append(i)
    return diff
    
