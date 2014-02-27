from math import sqrt
from itertools import takewhile

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

answer = sum(
    takewhile(
        lambda x: x < 2000000,
        prime_sequence()
    )
)

print(answer)