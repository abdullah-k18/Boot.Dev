def remove_duplicates(spells):
    seen = set()
    new_list = []
    for spell in spells:
        seen.add(spell)
    for s in seen:
        new_list.append(s)
    return new_list

