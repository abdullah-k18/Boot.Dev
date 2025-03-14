def meditate(mana, max_mana, energy, energy_drinks):
    while mana < max_mana and ((energy != 0) or (energy_drinks != 0)):
        if energy == 0 and energy_drinks >= 1:
            energy += 50
            energy_drinks -= 1
        else:
            mana += 1
            energy -= 1
        
    return mana, energy, energy_drinks
