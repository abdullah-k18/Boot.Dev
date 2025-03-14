def take_magic_damage(health, resist, amp, spell_power):
    total_damage = spell_power * amp
    actual_damage = max(0, total_damage - resist)
    new_health = max(0, health - actual_damage)
    return new_health

