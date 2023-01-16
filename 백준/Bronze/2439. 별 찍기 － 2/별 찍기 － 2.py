_qty = int(input())

for _seq in range(1, _qty + 1):
    print(f"{' ' * (_qty - _seq)}{'*' * _seq}")