def fibonacci_numbers():
    x, y = 1, 2
    while True:
        yield x
        x, y = y, x + y

answer = 0
for fib in fibonacci_numbers():
    if fib % 2 == 0:
        answer += fib
    if fib > 4000000:
        break

print(answer)