def get_character_record(name, server, level, rank):
    id = name + "#" + server
    dict = {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": id
        }

    return dict

