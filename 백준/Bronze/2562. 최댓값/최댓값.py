number_list = []
for _seq in range(9):
    number_list.append(int(input()))

print(max(number_list))
print(number_list.index(max(number_list)) + 1)