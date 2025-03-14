def get_avg_brand_followers(all_handles, brand_name):
    count = 0
    if len(all_handles) == 0:
        return 0
    for i in range(len(all_handles)):
        for j in range(len(all_handles[i])):
            if brand_name in all_handles[i][j]:
                count += 1
    avg = count / len(all_handles)
    return avg
