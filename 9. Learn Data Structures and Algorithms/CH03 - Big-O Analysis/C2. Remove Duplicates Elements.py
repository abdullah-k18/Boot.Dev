def remove_duplicates(nums):
    arr = []
    for i in nums:
        if i not in arr:
            arr.append(i)
        else:
            i += 1
    return arr
