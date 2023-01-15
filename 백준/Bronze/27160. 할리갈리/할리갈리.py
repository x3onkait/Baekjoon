# get input
card_qty      = int(input())
card_list     = []

for _seq in range(card_qty):
    card_list.append(input())

sorted_dict  = {}

for _each_card in card_list:
    name = _each_card.split(' ')[0]
    qty  = int(_each_card.split(' ')[1])
    
    if name in sorted_dict.keys():
        sorted_dict[name] += qty
    else:
        sorted_dict[name] = qty


if 5 in sorted_dict.values():
    print("YES")
else:
    print("NO")