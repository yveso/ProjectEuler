border = 1000
answer = str(sum(x ** x for x in range(1, border + 1)))[-10:]

print(answer)