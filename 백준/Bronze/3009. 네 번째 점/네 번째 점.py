position = []

for _seq in range(2 + 1):
    _x, _y = map(int, input().split())
    position.append([_x, _y])

_missing_x = position[0][0] ^ position[1][0] ^ position[2][0]
_missing_y = position[0][1] ^ position[1][1] ^ position[2][1]

print(f"{_missing_x} {_missing_y}")