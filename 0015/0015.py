"""
Every route will have 40 moves in total
Every route will have 20 moves to the bottom (and 20 to the right)
How many combinations of 20 moves to the bottom within 40 total moves exist?
Binomial coefficient ftw!
"""
from math import factorial

def binomial_coefficient(n, k):
    """Binomial coefficient, n choose k"""
    return factorial(n) / (factorial(k) * factorial(n - k))


answer = int(binomial_coefficient(40, 20))

print(answer)