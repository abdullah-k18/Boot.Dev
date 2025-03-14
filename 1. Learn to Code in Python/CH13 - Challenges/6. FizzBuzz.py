def fizzbuzz(start, end):
    array = []
    for i in range(start, end):
        if (((i % 3) == 0) and ((i % 5) == 0)):
            array.append("fizzbuzz")
        elif (i % 3) == 0:
            array.append("fizz")
        elif (i % 5) == 0:
            array.append("buzz")
        else:
            array.append(i)
    return array
