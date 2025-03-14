def get_follower_prediction(follower_count, influencer_type, num_months):
    if influencer_type == "fitness":
        growth_rate = 4
    elif influencer_type == "cosmetic":
        growth_rate = 3
    else:
        growth_rate = 2
    
    followers = follower_count * (growth_rate ** num_months)
    return followers
