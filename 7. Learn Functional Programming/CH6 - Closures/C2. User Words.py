def user_words(initial_words):
    arr = list(initial_words)
    def add_word(word):
        arr.append(word)
        tup = tuple(arr)
        return tup

    return add_word

