def get_estimated_spread(audiences_followers):
    num_followers = len(audiences_followers)
    sum = 0
    if len(audiences_followers) == 0:
        return 0
    for i in audiences_followers:
        sum = sum + i
    average_audience_followers = sum / len(audiences_followers)
    estimated_spread = average_audience_followers * (num_followers ** 1.2)
    return estimated_spread
