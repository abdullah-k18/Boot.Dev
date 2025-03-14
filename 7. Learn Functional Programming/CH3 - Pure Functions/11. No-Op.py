def remove_emphasis_from_word(word):
    if word.startswith("*") or word.endswith("*"):
        word = word.replace("*", "")
        return word
    else:
        return word


def remove_emphasis_from_line(line):
    splitting = line.split(" ")
    for i in range(len(splitting)):
        splitting[i] = remove_emphasis_from_word(splitting[i])
    splitting = " ".join(splitting)
    return splitting


def remove_emphasis(doc_content):
    function = remove_emphasis_from_line(doc_content)
    return function    
