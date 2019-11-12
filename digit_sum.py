def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10

    return total
