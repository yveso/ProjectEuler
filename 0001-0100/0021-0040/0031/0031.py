#inspired by http://users.softlab.ntua.gr/~ttsiod/euler31.html
coins = [1, 2, 5, 10, 20, 50, 100, 200]
goal = 200

lookup_matrix = {}

for val in range(0, goal + 1):
    lookup_matrix[(val, 0)] = 1

for y in range(0, goal + 1):
    for x in range(1, len(coins)):
        lookup_matrix[(y, x)] = lookup_matrix[(y, x - 1)]
        if y >= coins[x]:
            lookup_matrix[(y, x)] += lookup_matrix[(y - coins[x], x)]

answer = lookup_matrix[(goal, len(coins) - 1)]
print(answer)