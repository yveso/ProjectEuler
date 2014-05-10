def is_pythagorean_triplet(tup):
    return tup[0] ** 2 + tup[1] ** 2 == tup[2] ** 2

def all_possible_triplets():
    for a in range(1, 250):
        for b in range(a, 500):
            c = 1000 - a - b
            yield (a, b, c)

the_one = ()
for triplet in all_possible_triplets():
    if is_pythagorean_triplet(triplet):
        the_one = triplet
        break;

answer = the_one[0] * the_one[1] * the_one[2]

print(answer)