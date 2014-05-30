def sum_digits(number):
    total = 0
    while number:
        total, number = total + number % 10, number / 10
    return total

border = 100
answer = max([sum_digits(a ** b) 
    for a in range(border) for b in range(border)])

print(answer)