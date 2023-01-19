_number = int(input())

for _seq in range(1, _number + 1):

    _temp = list(map(int, str(_seq)))
    _trial = _seq + sum(_temp)

    if _trial == _number:
        print(_seq)
        break

    if _seq == _number:
        print(0)            # no initiator 