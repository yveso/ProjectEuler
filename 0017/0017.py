dict_below_20 = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

dict_tens = {
  2: "twenty",
  3: "thirty",
  4: "forty",
  5: "fifty",
  6: "sixty",
  7: "seventy",
  8: "eighty",
  9: "ninety"
}

def wordy_below_100(number):
    if number < 20:
        return dict_below_20[number]
    else:
        ten = number // 10
        one = number % 10
        word = dict_tens[ten]
        if one != 0:
            word += dict_below_20[one]
        return word

def wordy_number(number):
    word = ""
    if number < 100:
        word = wordy_below_100(number)
    elif number < 1000:
        hundred = number // 100
        rest = number % 100
        word = dict_below_20[hundred] + "hundred" 
        if rest != 0:
            word += "and" + wordy_below_100(rest)
    else:
        word = "onethousand"
    return word

answer = 0
for i in range(1, 1001):
    w = wordy_number(i)
    answer += len(w)

print(answer)