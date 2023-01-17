_target = int(input())

button_5M = button_1M = button_10S = -1

if _target % 10 != 0:       # unsolvable
    print("-1")
else:
    button_5M = _target // 300
    button_1M = (_target % 300) // 60
    button_10S = ((_target % 300) % 60) // 10
    print(f"{button_5M} {button_1M} {button_10S}")