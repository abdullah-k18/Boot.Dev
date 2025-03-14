import math

def get_influencer_score(num_followers, average_engagement_percentage):
    followers = math.log(num_followers, 2)
    influencer_score = average_engagement_percentage * followers
    return influencer_score
