_qty = int(input())

for _seq in range(_qty):
    
    standby_profit, advertisement_profit, advertisement_cost = map(int, input().split())

    if standby_profit > advertisement_profit - advertisement_cost:
        print("do not advertise")
    elif standby_profit == advertisement_profit - advertisement_cost:
        print("does not matter")
    else:
        print("advertise")