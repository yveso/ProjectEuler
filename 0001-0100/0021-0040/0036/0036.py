def is_palindrome(number):
    s = str(number)
    s_rev = s[::-1]
    return s == s_rev

total = 0
for i in range(1, 1000000):
    if is_palindrome(i):
        binary = bin(i).lstrip("0b")
        if is_palindrome(binary):
            total += i

print(total)