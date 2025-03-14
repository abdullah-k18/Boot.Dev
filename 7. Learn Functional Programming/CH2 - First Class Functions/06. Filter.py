def remove_invalid_lines(document):
    lines = document.split("\n")
    for i in lines:
        if i.startswith("-"):
            lines.remove(i)
    joined = "\n".join(lines)
    return joined
