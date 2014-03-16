from itertools import permutations

all_permutations = permutations(range(10), 10)
millionth = list(all_permutations)[999999]
answer = "".join([str(x) for x in millionth])

print(answer)