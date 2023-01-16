import re

_trials = int(input())

for _seq in range(_trials):
    _oxstring       = input()
    _oxlist_splited = [iters.group(0) for iters in re.finditer(r"(\D)\1*", _oxstring)]

    # accumulate score
    score = 0
    for _inspect in _oxlist_splited:
        if "X" in _inspect:
            pass
        else:
            score += len((_inspect) * (len(_inspect) + 1)) / 2
    print(int(score))