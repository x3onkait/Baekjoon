input()    # ignore the first input
number_list = list(input())

accumulated = 0
for _digit in number_list:
    accumulated += int(_digit)

print(accumulated)