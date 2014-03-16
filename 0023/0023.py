from math import sqrt

def sum_of_divisors(number):
    s_o_d = 1
    root = int(sqrt(number))
    for i in range(2, root + 1):
        if number % i == 0:
            s_o_d += i
            s_o_d += number / i
    if root == sqrt(number):
        s_o_d -= root
    return s_o_d

def is_abundant(number):
    return sum_of_divisors(number) > number

total = 0
abundant_numbers = set()
limit = 28123

for i in range(1, limit + 1):
    if is_abundant(i):
        abundant_numbers.add(i)
    if not any((i - other in abundant_numbers) for other in abundant_numbers):
        total += i

print(total)