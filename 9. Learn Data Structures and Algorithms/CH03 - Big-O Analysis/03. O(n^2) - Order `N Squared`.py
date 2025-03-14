def does_name_exist(first_names, last_names, full_name):
    for i in first_names:
        for j in last_names:
            if (i + " " + j) == full_name:
                return True
    return False

