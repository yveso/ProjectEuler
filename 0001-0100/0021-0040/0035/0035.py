def sieve_list(upper_bound):
    prime_list = [True] * upper_bound
    prime_list[0] = False
    prime_list[1] = False

    for i, is_prime in enumerate(prime_list):
        if is_prime:
            for j in range(i*i, upper_bound, i):
                prime_list[j] = False

    return prime_list


def to_digits(number):
    n = int(str(number)[::-1])
    while n:
        yield n % 10
        n //= 10


def from_digits(digits):
    sum = 0
    for i, d in enumerate(reversed(digits)):
        sum += 10**i * d
    return sum


def is_circular_prime(prime, prime_list):
    circles = []
    digits = list(to_digits(prime))
    for i in range(len(digits)):
        rotation = from_digits(digits[i:] + digits[:i])
        circles.append(rotation)
    return all(prime_list[i] for i in circles)

prime_list = sieve_list(10**6)
counter = 0
for i, is_prime in enumerate(prime_list):
    if is_prime and is_circular_prime(i, prime_list):
        counter += 1
print(counter)
