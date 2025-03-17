def power_set(input_set):
    if len(input_set) == 0:
        return [[]]
    else:
        arr = [[]]
        for i in input_set:
            arr1 = []
            for subset in arr:
                arr1.append(subset + [i])
            arr.extend(arr1)
        return arr
