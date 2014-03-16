def get_names(path):
    with open(path) as f:
        str = f.read()
    return [x.strip('"') for x in str.split(",")]

def alphabetical_value(name):
    return sum([ord(x) - 64 for x in list(name)])

names = get_names("names.txt")
names.sort()

total = 0
for i in range(len(names)):
    pos = i + 1
    score = pos * alphabetical_value(names[i])
    total += score

print(total)