input()                 # ignore

vote_casted = list(input())

_qty_A = vote_casted.count('A')
_qty_B = vote_casted.count('B')

result = "A" if _qty_A > _qty_B else "B" if _qty_A < _qty_B else "Tie"

print(result)