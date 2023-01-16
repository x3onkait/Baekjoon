def get_divisors(input):

    divisors_list = []

    # more efficiently...
    for _seq in range(1, int(input ** 0.5) + 1):        # search until "sqrt(n) + 1"
        if input % _seq == 0:
            divisors_list.append(_seq)
            if (_seq ** 2 != input):
                divisors_list.append(input // _seq)

    divisors_list.sort()

    return divisors_list

number, order = map(int, input().split())
try:
    print(f"{get_divisors(number)[order - 1]}")
except IndexError:
    print("0")