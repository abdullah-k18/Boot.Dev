def change_bullet_style(document):
    string = document.split("\n")
    for i, index in enumerate(string):
        string[i] = convert_line(index)
    rejoin = "\n".join(string)
    return rejoin

# Don't edit below this line

def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line

