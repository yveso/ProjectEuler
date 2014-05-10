def prime_factors(number):
    factors, i, = [], 2
    while i <= number:
        if number % i == 0:
            number /= i
            factors.append(i)
        else:
            i += 1
    return factors

all_yet_occured_factors = []
for i in range(20, 2, -1):
    tmp_factors = all_yet_occured_factors[:]
    all_current_factors = prime_factors(i)
    new_occured_factors_buffer = []
    for factor in all_current_factors:
        if factor in tmp_factors:
            tmp_factors.remove(factor)
        else:
            new_occured_factors_buffer.append(factor)
    all_yet_occured_factors.extend(new_occured_factors_buffer)

answer = reduce(
    lambda x, y: x * y,
    all_yet_occured_factors
)

print(answer)