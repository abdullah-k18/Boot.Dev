def num_possible_orders(num_posts):
    fact = 1
    for i in range(num_posts, 1, -1):
        fact *= i
    return fact
