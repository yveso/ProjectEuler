def fibonacci_sequence():
    first, second = 1, 1
    yield second
    while True:
        yield second
        first, second = second, first + second

fib = fibonacci_sequence()
index = 0

while True:
    f = next(fib)
    index += 1
    if f > 10 ** 999:
        break

print(index)