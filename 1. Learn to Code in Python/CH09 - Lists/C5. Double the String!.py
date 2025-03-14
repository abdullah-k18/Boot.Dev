def double_string(string):
    sentence = []
    for i in range(0, len(string)):
        sentence.append(string[i]*2)
        
    var = "".join(sentence)
    return var
