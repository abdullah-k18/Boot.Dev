def find_minimum(nums):
    min = float("+inf")
    if len(nums) == 0:
        return None
    else:
        for i in nums:
            if i < min:
                min = i
        return min
