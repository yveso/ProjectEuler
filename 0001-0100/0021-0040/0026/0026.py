'''
If we divide on paper, a recurring cycle would appear, if a value for
a subdivision appears for a second time.
So for each step in a manual calculation divide_by_hand gives us the result
and the value for the next sub division. The later would be sufficient.

Then recurring_cycle_length will check, when a known value appears.
If a calculation terminates, 0 will be returned. As the problem only affects
rational numbers (that terminate or have a cricle), the could will terminate.
'''


def divide_by_hand(number):
    nxt = 10
    while nxt != 0:
        out = nxt // number
        nxt = (nxt - number * out) * 10
        yield (out, nxt)


def recurring_cycle_length(number):
    seen_values = []
    for i, act in enumerate(divide_by_hand(number)):
        if act[1] in seen_values:
            return i
        seen_values.append(act[1])
    return 0

max_value = 0
max_length = 0
for i in range(1, 1001):
    act = recurring_cycle_length(i)
    if act > max_length:
        max_length = act
        max_value = i
        # print('Found new: {0} with length {1}'.format(max_value, max_length))
print(max_value)
