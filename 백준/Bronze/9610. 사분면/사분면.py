_qty = int(input())

Q1 = Q2 = Q3 = Q4 = borderline = 0

for _seq in range(_qty):

    _x, _y = map(int, input().split())

    if   _x > 0 and _y > 0:
        Q1 += 1
    elif _x < 0 and _y > 0:
        Q2 += 1
    elif _x < 0 and _y < 0:
        Q3 += 1
    elif _x > 0 and _y < 0:
        Q4 += 1
    else:
        borderline += 1

print(f"Q1: {Q1}")
print(f"Q2: {Q2}")
print(f"Q3: {Q3}")
print(f"Q4: {Q4}")
print(f"AXIS: {borderline}")