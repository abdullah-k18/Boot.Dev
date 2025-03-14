def join_strings(strings):
    single_string = ""
    for i in range(0, len(strings)):
        if i == len(strings)-1:
            single_string += strings[i]
        else:
            single_string += strings[i] +","
    return single_string
