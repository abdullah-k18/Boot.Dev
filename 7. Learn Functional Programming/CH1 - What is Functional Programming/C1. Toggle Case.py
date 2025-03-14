def toggle_case(line):
    if line.istitle():
        line = line.upper()
        return line + "!!!"
    if line.isupper():
        line = line.lower()
        line = line.capitalize()
        line = line.replace("!", "")
        return line
    if len(line) > 0 and line[1:].islower():
        line = line.title()
        return line
    else:
        return line

