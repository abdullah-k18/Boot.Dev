def merge(dict1, dict2):
    dict1.update(dict2)
    return dict1
    

def total_score(score_dict):
    total = 0
    for i in score_dict:
        total += score_dict[i]
    return total


