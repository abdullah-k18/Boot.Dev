def median_followers(nums):
    nums = sorted(nums)
    div = len(nums) // 2
    if len(nums) == 0:
        return None
    elif (len(nums) % 2) == 0:
        return (nums[div - 1] + nums[div]) / 2
    else:
        return nums[div]
