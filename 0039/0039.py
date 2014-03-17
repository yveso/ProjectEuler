max_perimeter, max_count, p = 1000, 0, 0

for perimeter in range(10, max_perimeter + 1):
    min_hypotenuse = 2
    count = 0
    for hypo in range(min_hypotenuse, max_perimeter - 1):
        rest = perimeter - hypo
        for leg1 in range(1, rest / 2): # /2 because of symmetry
            leg2 = rest - leg1
            if hypo ** 2 == leg1 ** 2 + leg2 ** 2:
                count += 1
    if count > max_count:
        max_count = count
        p = perimeter

print(p)