_qty = int(input())

if _qty == 0:
    print("1")
else:
    result = 1
    for _seq in range(1, _qty + 1):
        result *= _seq
    print(result)