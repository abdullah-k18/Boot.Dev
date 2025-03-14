def get_common_formats(formats1, formats2):
    set1 = set()
    set2 = set()
    for i in formats1:
        set1.add(i)
    for i in formats2:
        set2.add(i)
    n = set1. intersection(set2)
    return n
    

