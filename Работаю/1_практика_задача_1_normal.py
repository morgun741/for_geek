digit = int(input())
m = 0
while digit > 0:
    if digit % 10 > m:
        m = digit % 10
    digit //= 10
print(m)