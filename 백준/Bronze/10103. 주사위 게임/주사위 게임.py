_qty = int(input())

p1 = p2 = 100

for _seq in range(_qty):
    dice_p1, dice_p2 = map(int, input().split())
    if   dice_p1 > dice_p2:
        p2 -= dice_p1
    elif dice_p1 < dice_p2:
        p1 -= dice_p2
    else:
        pass

print(f"{p1}\n{p2}")