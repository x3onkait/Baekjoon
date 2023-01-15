_x = int(input())
_y = int(input())

if _x > 0 and _y > 0:
    print("1")
elif _x > 0 and _y < 0:
    print("4")
elif _x < 0 and _y > 0:
    print("2")
else:
    print("3")