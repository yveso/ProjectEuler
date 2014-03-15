def d(number):
    return sum(
        filter(
            lambda x: number % x == 0,
            [x for x in range(1, number / 2 + 1)]
        )
    )

answer = sum(
    filter(
        lambda x: d(d(x)) == x and d(x) != x,
        [x for x in range(1, 10001)]
    )
)

print(answer)