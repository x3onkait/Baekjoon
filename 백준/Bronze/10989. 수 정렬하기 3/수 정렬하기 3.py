import sys

trial = int(input())

numbers = [0] * (10000 + 1)         # because the number of list starts from ZERO(0)

# get input
for _seq in range(trial):
    input = int(sys.stdin.readline())
    numbers[input] += 1

for _seq in range(len(numbers)):
    if numbers[_seq] != 0:
        for _print in range(numbers[_seq]):
            print(_seq)