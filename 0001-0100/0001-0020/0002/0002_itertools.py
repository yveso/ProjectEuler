from itertools import takewhile

def fibonacci_numbers():
    x, y = 1, 2
    while True:
        yield x
        x, y = y, x + y

answer = sum(
    filter(
        lambda x: x % 2 == 0, 
        takewhile(lambda x: x <= 4000000, fibonacci_numbers())
    )
)

print(answer)