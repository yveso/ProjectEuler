"""
not the fastest, but runs under a minute
"""
import time

def loop_once(number):
    """
    returns a tuple with
    [0] -> sum of the squared digits, eg 82 -> 8**2 + 2**2 = 64 + 4 = 68
    [1] -> an tuple with the counts of the digits
        eg 12333300 -> (2, 1, 1, 4, 0, 0, ... 0) (two zeros, 1 one, 1 two, 4 threes)
    as eg 1234 and 4321 will have the same squared digit sum, we'll cache those
    digit-counts instead of the number
    one function to run the digit-split-loop just once (hence the name)
    """
    sq_sum = 0
    digits = [0] * 10
    while number:
        d = number % 10
        sq_sum += (d * d)
        digits[d] += 1
        number /= 10
    return (sq_sum, tuple(digits))

cache_one = set([loop_once(1)[1]])
cache_eighty_nine = set([loop_once(89)[1]])

def is_eighty_nine_number(number):
    chain = []
    n = number
    n_dig_rep = loop_once(number)[1]
    while True:
        if n == 89 or n_dig_rep in cache_eighty_nine:
            cache_eighty_nine.add(n_dig_rep)
            for c in chain:
                cache_eighty_nine.add(c)
            return True
        elif n == 1 or n_dig_rep in cache_one:
            cache_one.add(n_dig_rep)
            for c in chain:
                cache_one.add(c)
            return False
        else:
            tmp = loop_once(n)
            n = tmp[0]
            n_dig_rep = tmp[1]
            chain.append(n_dig_rep)

t1 = time.clock()
count = 0
for i in reversed(range(1, 10**7)):
    if is_eighty_nine_number(i):
        count += 1
t2 = time.clock()

print(count, t2-t1)
