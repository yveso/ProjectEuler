def is_palindrome(number):
    return str(number) == str(number)[::-1]

answer = 0

for x in range(100, 1000):
    for y in range(x, 1000):
        current = x * y
        if is_palindrome(current) and current > answer:
            answer = current

print(answer)
