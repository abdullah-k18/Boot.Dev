def average_followers(nums):
    sum = 0
    if len(nums) == 0:
        return None
    for i in nums:
        sum = sum + i
        average = sum / len(nums)
    return average

