def file_type_getter(file_extension_tuples):
    dict1 = {}
    dict2 = {}
    for i in range(len(file_extension_tuples)):
        dict1[file_extension_tuples[i][0]] = file_extension_tuples[i][1]
    for i, value in enumerate(dict1):
      dict2[dict1[value][i]] = value
      dict2[dict1[value][i - 1]] = value

    file_name = lambda file: dict2.get(file, "Unknown")
    return file_name
