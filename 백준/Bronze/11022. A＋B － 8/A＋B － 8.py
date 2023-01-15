_qty = int(input())

result = ""

for _seq in range(_qty):
    n1, n2 = map(int, input().split())
    result += f"Case #{_seq + 1}: {n1} + {n2} = {n1 + n2}\n"

print(result)