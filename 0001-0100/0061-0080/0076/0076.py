#see Problem 31
integers = list(range(1,100))
goal = 100

lookup_matrix = {}

for val in range(0, goal + 1):
    lookup_matrix[(val, 0)] = 1

for y in range(0, goal + 1):
    for x in range(1, len(integers)):
        lookup_matrix[(y, x)] = lookup_matrix[(y, x - 1)]
        if y >= integers[x]:
            lookup_matrix[(y, x)] += lookup_matrix[(y - integers[x], x)]

answer = lookup_matrix[(goal, len(integers) - 1)]
print(answer)