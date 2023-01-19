while True:

    side_length_list = list(map(int, input().split()))

    if side_length_list == [0, 0, 0]:
        break

    _z     = max(side_length_list)
    side_length_list.remove(_z)
    _x, _y = map(int, side_length_list)

    if _z ** 2 == _x ** 2 + _y ** 2:
        print("right")
    else:
        print("wrong")