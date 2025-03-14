def is_prime(number):
    if number < 2:
        return False
    elif number >= 2:
        for i in range(2, (number//2)+1):
            if (number % i) == 0:
                return False
        return True
