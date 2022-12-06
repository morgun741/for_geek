
def is_prime_number(number: int):
    list_enumere = [i for i in range(number)]
    work_digits = []
    a = False
    b = True
    digit = 0
    for i in range(len(list_enumere)):
        if list_enumere[i] != 0 and list_enumere[i] != 1:
            work_digits.append(list_enumere[i])
    for i in range(2, len(work_digits)):
        digit += (1 if number%i == 0  else 0)
        return digit == 0
def get_next_prime_number(number: int):
    i = number
    while True:
        i += 1
        if is_prime_number(i) is True or is_prime_number(i) is None:
            return i
            exit()
        else:
            continue

a = is_prime_number(9)
print(a)