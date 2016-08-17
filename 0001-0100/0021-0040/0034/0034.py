'''
Upper bound is a 7 digit number.
7 * 9! = 2,540,160
8 * 9! = 2,903,040
'''
from math import factorial

fact_cache = {i: factorial(i) for i in range(10)}


def sum_of_digits_factorial(number):
    sum = 0
    while number:
        sum += fact_cache[number % 10]
        number //= 10
    return sum


def is_curious(number):
    return number == sum_of_digits_factorial(number)

print(sum([i for i in range(10, 10**6) if is_curious(i)]))
