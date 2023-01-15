dice_result = list(map(int, input().split()))
dice_result.sort()

if len(dice_result) - len(set(dice_result)) == 2:           # 3 EQUAL. jackpot
    print(10000 + dice_result[0] * 1000)
elif len(dice_result) - len(set(dice_result)) == 1:         # 2 EQUAL.
    if dice_result[0] == dice_result[1]:
        print(1000 + dice_result[0] * 100)
    else:
        print(1000 + dice_result[1] * 100)
else:                                                       # NOT EQUAL.
    print(100 * dice_result[2])