card_qty    = int(input())
card_list   = list(map(int, input().split()))

sorted_list = []
temp = []

for _seq in range(card_qty):

    try:
        if card_list[_seq + 1] - card_list[_seq] == 1:
            temp.append(card_list[_seq])
        else:
            temp.append(card_list[_seq])
            sorted_list.append(temp)
            temp = []

    except IndexError:
        # if we try to compare something at the last step, the IndexError will occur
        # so wee need to treat differently for this special case.
        if card_list[_seq] - card_list[_seq - 1] == 1:
            temp.append(card_list[_seq])
            sorted_list.append(temp)
        else:
            temp = []
            temp.append(card_list[_seq])
            sorted_list.append(temp)

score = 0
for _number in sorted_list:
    score += _number[0]

print(score)