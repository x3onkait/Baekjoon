numbers = []
for _seq in range(10):
    numbers.append(int(input()))

print(len(set(list(map(lambda x: x % 42, numbers)))))