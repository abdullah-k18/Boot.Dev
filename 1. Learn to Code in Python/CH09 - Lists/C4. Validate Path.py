def validate_path(expected_path, character_path):
    percentage = 0
    count = 0
    for i in character_path:
        if i in expected_path:
            count +=1

    percentage = (count / len(expected_path)) * 100
    return character_path[0], percentage

