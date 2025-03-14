def map_keywords(document, document_map):
    document_map = document_map.copy()
    if document in document_map:
        return document_map[document], document_map
    found_keywords = find_keywords(document)
    document_map[document] = found_keywords
    return found_keywords, document_map


def find_keywords(document):
    keywords = [
    "functional",
    "immutable",
    "declarative",
    "higher-order",
    "lambda",
    "deterministic",
    "side-effects",
    "memoization",
    "referential transparency",
    ]

    substrings = []
    document = document.lower()

    for i in range(len(keywords)):
        if keywords[i] in document:
            substrings.append(keywords[i])
    return substrings

    pass

