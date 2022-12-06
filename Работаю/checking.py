def is_prime_number(number: int) -> bool:
    """Returns True, if `number` is prime, otherwise returns False"""
    divisions_count = 0
    for divider in range(2, number):
        divisions_count += (1 if number % divider == 0 else 0)
    return divisions_count == 0
a = is_prime_number(9)
print(a)