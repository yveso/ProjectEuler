# Multiplicand, multiplier, and product need to have 9 digits in total.
# 1 digit * 2 digits = 2 digits (eg 1*10) or 3 digits (eg 2*99),
# That leads to:
# 1 digit * 4 digits = 4 digits
# 2 digits * 3 digits = 4 digits


def possible_products(number):
    for i in range(2, 100):
        if number % i == 0:
            yield (number, i, number // i)


def is_valid(product_tuple):
    as_string = str(product_tuple[0]) + \
        str(product_tuple[1]) + \
        str(product_tuple[2])
    if len(as_string) != 9 or '0' in as_string:
        return False
    return len(set(list(as_string))) == 9


if __name__ == '__main__':
    products = []
    for i in range(10**3, 10**4):
        for pp in possible_products(i):
                if is_valid(pp):
                    products.append(pp[0])
                    break
    print(sum(products))
