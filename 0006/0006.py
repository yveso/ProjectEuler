def sum_of_squares(number):
    return sum(x * x for x in range(1, number + 1))

def squared_sum(number):
    sum = number * (number + 1) / 2
    return sum * sum

answer = squared_sum(100) - sum_of_squares(100)

print(answer)