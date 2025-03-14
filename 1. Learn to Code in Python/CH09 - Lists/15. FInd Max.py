def find_max(nums):
    max_so_far = float("-inf")

    for i in range(len(nums)):
        if nums[i] > max_so_far:
            max_so_far = nums[i]
    return max_so_far

