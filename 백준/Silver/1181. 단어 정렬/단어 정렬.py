import sys

_qty      = int(input())
word_list = []

for _seq in range(_qty):
    word_list.append(sys.stdin.readline().strip())

word_list = list(set(word_list))
word_list.sort(key = lambda x : (len (x), x))       # multiple criteria, step-by-step.

for _sorted in word_list:
    print(_sorted)