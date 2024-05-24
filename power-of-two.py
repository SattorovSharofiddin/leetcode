def is_power_of_two(n):
    if n < 0:
        return False
    if bin(n).count('1') == 1:
        return True
    return False


print(is_power_of_two(16))
