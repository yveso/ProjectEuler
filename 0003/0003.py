def prime_factors(number):
    factors, i, = [], 2
    while i <= number:
        if number % i == 0:
            number /= i
            factors.append(i)
        else:
            i += 1
    return factors

answer = max(prime_factors(600851475143))

print(answer)