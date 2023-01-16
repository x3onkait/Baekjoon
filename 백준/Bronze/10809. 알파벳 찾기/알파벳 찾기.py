import string

word     = input()
position = dict.fromkeys(string.ascii_lowercase, -1)

for _alphabet in word:
    if position[_alphabet] == -1:
        position[_alphabet] = word.index(_alphabet)
    else:
        pass

print(' '.join(f"{value}" for value in position.values()))