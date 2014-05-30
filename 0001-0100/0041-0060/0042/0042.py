def word_score(word):
    score = 0
    for c in word:
        score += (ord(c) - 64)
    return score

t = lambda n: n * (n + 1) / 2

triangle_numbers = [ t(n) for n in range(1, 10) ]

def is_triangle_word(word):
    score = word_score(word)
    if score > max(triangle_numbers):
        index = len(triangle_numbers)
        while True:
            next_triangle = t(index)
            triangle_numbers.append(next_triangle)
            index += 1
            if next_triangle > score:
                break
    return score in triangle_numbers

with open('words.txt', 'r') as file:
    words = [ w.strip('"') for w in file.read().split(',')]

answer = len(filter(is_triangle_word, words))

print(answer)