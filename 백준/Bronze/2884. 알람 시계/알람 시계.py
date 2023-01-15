_hour, _minute = map(int, input().split())

if _minute - 45 < 0:
    _hour   -= 1
    _minute += 15

    if _hour < 0:
        _hour = 23
else:
    _minute -= 45

print(f"{_hour} {_minute}")