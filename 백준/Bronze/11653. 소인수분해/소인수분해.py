target = int(input())
_try   = 2 # divide since 2

while _try <= target:
    while(target % _try == 0):
        target /= _try
        print(_try)
    _try += 1