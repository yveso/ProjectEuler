#inspired by http://code.jasonbhill.com/c/project-euler-problem-14/
border, max_length, answer = 1000000, 0, 0
collatz_map = [0] * border
collatz_map[1] = 1

for i in range(1, border):
    next, length = i, 0
    yet_unknown = []
    while next > border - 1 or collatz_map[next] == 0:
        yet_unknown.append(next)

        next = (next / 2) if next % 2 == 0 else (3 * next + 1)

        length += 1
    for j in range(length):
        new_one = yet_unknown[j]
        if new_one < border:
            new_length = collatz_map[next] + (length - j)
            collatz_map[new_one] = new_length
            if new_length > max_length:
                max_length = new_length
                answer = new_one

print(answer)