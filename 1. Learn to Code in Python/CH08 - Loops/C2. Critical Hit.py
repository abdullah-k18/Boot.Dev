def calculate_flurry_crit(num_attacks, base_damage):
    total_damage = 0
    last = 0
    for i in range(0, num_attacks):
        print(i)
        if i == num_attacks - 1:
            last += 4 * base_damage
        else:
            total_damage += 2 * base_damage
    return last + total_damage
                

