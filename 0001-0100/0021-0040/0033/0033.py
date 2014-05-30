all_fractions = [(n, d) for n in range(11, 100) for d in range(n + 1, 100)]

digits = lambda number: map(int, str(number))
other = lambda digits, is_not: \
    [x for x in digits if x != is_not][0] if digits[0] != digits[1] else is_not
equal_fractions = lambda t1, t2: float(t1[0]) / t1[1] == float(t2[0]) / t2[1]

def curious_filter(tuple):
    nom_digits, denom_digits = digits(tuple[0]), digits(tuple[1])
    is_curious = False
    for d in nom_digits:
        if d in denom_digits and d != 0:
            other_digits = (other(nom_digits, d), other(denom_digits, d))
            if other_digits[1] != 0 and equal_fractions(tuple, other_digits):
                is_curious = True
    return is_curious

def result_fraction(tuples):
    numerator, denominator = 1, 1
    for t in tuples:
        numerator *= t[0]
        denominator *= t[1]
    return (numerator, denominator)

def reduce_fraction(tuple):
    numerator, denominator = tuple[0], tuple[1]
    for i in range(2, numerator + 1):
        while numerator % i == 0 and denominator % i == 0:
            numerator /= i
            denominator /= i
    return (numerator, denominator)

answer = reduce_fraction(
    result_fraction(
        filter(curious_filter, all_fractions)
    )
)[1]

print(answer)