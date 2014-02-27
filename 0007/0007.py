from math import sqrt
from itertools import islice

def prime_sequence():
    yield 2
    current_number_to_check = 3
    while True:
        found_a_divisor = False
        sqrt_of_current =  int(sqrt(current_number_to_check))
        for i in range(3, sqrt_of_current + 1, 2):
            if current_number_to_check % i == 0:
                found_a_divisor = True
                break;
        if not found_a_divisor:
            yield current_number_to_check
        current_number_to_check += 2

#recipe for nth: http://docs.python.org/2/library/itertools.html#recipes
answer = next(islice(prime_sequence(), 10000, None), None)

print(answer)