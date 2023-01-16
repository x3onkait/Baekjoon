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

while True:

    number = int(input())

    if number != -1:
        divisors_list = get_divisors(number)
        divisors_list.pop()
        if number == sum(divisors_list):
            print(f"{number} = {' + '.join(map(str, divisors_list))}")
        else:
            print(f"{number} is NOT perfect.")
    else:
        break