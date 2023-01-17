import math

_x, _y, _w, _h = map(int, input().split())

print(min([_x, _y, _h - _y, _w - _x]))