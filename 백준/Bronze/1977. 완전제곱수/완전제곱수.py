import math

_mininum_limit = int(input())
_maximum_limit = int(input())

perfect_square_number_list = []

for _trial in range(_mininum_limit, _maximum_limit + 1):
    for _seq in range(1, int(math.sqrt(_trial)) + 1):
        if _seq ** 2 == _trial:
            perfect_square_number_list.append(_trial)
            break
        else:
            continue

if len(perfect_square_number_list) == 0:
    print("-1")
else:
    print(sum(perfect_square_number_list))
    print(min(perfect_square_number_list))