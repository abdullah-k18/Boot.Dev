def get_median_font_size(font_sizes):
    new_array = font_sizes.copy()
    new_array.sort()
    if len(font_sizes) == 0:
        return None
    elif ((len(new_array) % 2) == 0 ):
        num = int(len(new_array) / 2)
        num2 = int(num - 1)
        if new_array[num] < new_array[num2]:
            return new_array[num]
        elif new_array[num2] < new_array[num]:
            return new_array[num2]
        elif new_array[num] == new_array[num2]:
            return new_array[num]
    else:
        num = len(new_array) // 2
        return new_array[num]
    return new_array

