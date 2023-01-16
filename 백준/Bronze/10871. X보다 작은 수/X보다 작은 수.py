_qty, criteria = map(int, input().split())
number_lists   = list(map(int, input().split()))

result = ""
for _seq in range(_qty):
    if number_lists[_seq] < criteria:
        result += f"{number_lists[_seq]} "

print(result)