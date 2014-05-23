#could be faster, but problem solved
import math

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

lookup = {}

def quadratic_expression(n, a, b):
    return n * n + a * n + b

def prime_chain_length(a, b):
    counter, n = 0, 0
    while True:
        current_val = quadratic_expression(n, a, b)
        if current_val not in lookup:
            lookup[current_val] = is_prime(current_val)
        if lookup[current_val]:
            counter += 1
            n += 1
        else:
            return counter

best_length, best_a, best_b, = 0, 0, 0
for a in range(-999, 1000):
    for b in range(-999, 1000):
        if a == -79 and b == 1601:
            print "hui"
        current_length = prime_chain_length(a, b)
        if current_length > best_length:
            best_length, best_a, best_b = current_length, a, b

answer = best_a * best_b
print(answer)
