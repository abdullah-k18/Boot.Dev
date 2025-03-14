def restore_documents(originals, backups):
    originals_set = set()
    backups_set = set()
    for i in backups:
        if not i.isdigit(): 
            backups_set.add(i)
    for i in originals:
        if not i.isdigit():
            originals_set.add(i)
    orig = list(originals_set)
    backup = list(backups_set)
    for i in range(len(orig)):
        orig[i] = orig[i].upper()
    for i in range(len(backup)):
        backup[i] = backup[i].upper()
    combined = orig + backup
    combined = set(combined)
    return combined
