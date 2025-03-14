import functools


def join(doc_so_far, sentence):
    return doc_so_far + ". " + sentence


def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    else:
        slicing = sentences[:n]
        returning = functools.reduce(join, slicing)
        return returning + "."

