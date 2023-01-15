_joiner         = int(input())
score_list      = []

for _seq in range(_joiner):

    dice_result = list(map(int, input().split()))
    dice_result.sort()

    if len(dice_result) - len(set(dice_result)) == 2:           # 3 EQUAL. jackpot
        winning_money = 10000 + dice_result[0] * 1000
    elif len(dice_result) - len(set(dice_result)) == 1:         # 2 EQUAL.
        if dice_result[0] == dice_result[1]:
            winning_money = 1000 + dice_result[0] * 100
        else:
            winning_money = 1000 + dice_result[1] * 100
    else:                                                       # NOT EQUAL.
        winning_money = 100 * dice_result[2]

    score_list.append(winning_money)

score_list.sort(reverse = True)
print(score_list[0])