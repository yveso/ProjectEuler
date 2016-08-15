def sum_of_digits_fifth_power(n):
    sum = 0
    while n:
        sum += (n % 10)**5
        n //= 10
    return sum

if __name__ == '__main__':
    for count_digits in range(1, 10):
        max_possible_number = count_digits * 9**5
        print(count_digits, max_possible_number, len(str(max_possible_number)))
    # 7 digits can only add up to a six digit number.
    # So 6 digits is an upper bound.
    # Brute force
    valid_numbers = []
    for i in range(10, 10**6 - 1):
        sum_digits = sum_of_digits_fifth_power(i)
        if sum_digits == i:
            valid_numbers.append(sum_digits)
    print(sum(valid_numbers))
