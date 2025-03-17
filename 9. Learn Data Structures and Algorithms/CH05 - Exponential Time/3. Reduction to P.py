def fib(n):
    if n == 1:
        return 1
        
    current = 0
    parent = 1
    grand_parent = 0

    for i in range(n - 1):
        current = parent + grand_parent
        grand_parent = parent
        parent = current

    return current
