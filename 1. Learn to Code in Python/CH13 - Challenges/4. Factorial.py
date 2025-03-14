def find_min(nums):
    min = float("inf")
    for i in range(len(nums)):
        if nums[i] < min:
            min = nums[i]
    return min

