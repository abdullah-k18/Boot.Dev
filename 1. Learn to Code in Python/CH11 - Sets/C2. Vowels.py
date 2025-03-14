def count_vowels(text):
    count = 0
    vowels = set()
    for char in text:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
            count += 1
            vowels.add(char)
    print(vowels)
    return count, vowels

