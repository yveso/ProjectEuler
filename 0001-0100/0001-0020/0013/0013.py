lines = [line.rstrip("\n") for line in open("numbers.txt")]
sum = sum([int(x) for x in lines])

answer = str(sum)[:10]

print(answer)