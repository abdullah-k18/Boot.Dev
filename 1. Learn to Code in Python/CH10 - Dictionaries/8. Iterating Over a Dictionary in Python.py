def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    name = ""
    if len(enemies_dict) == 0:
        return None
    else:
        for enemy in enemies_dict:
            if enemies_dict[enemy] > max_so_far:
                max_so_far = enemies_dict[enemy]
                name = enemy
    return name

