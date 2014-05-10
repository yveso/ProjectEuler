from math import sqrt

def triangle_numbers():
    last = 0
    i = 1
    while True:
        last += i
        i += 1
        yield last

def count_divisors(number):
    count = 2
    number_sqrt = int(sqrt(number))
    for x in range(2, number_sqrt):
        if number % x == 0:
            count += 2
    if number % number_sqrt == 0:
        count += 1
    return count

tn = triangle_numbers()
while True:
    actual = next(tn)
    if count_divisors(actual) > 500:
        break

print(actual)