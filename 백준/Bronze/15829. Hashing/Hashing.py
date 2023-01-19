import string

_input_length = int(input())
_input_string = input()

value = 0

input_character = list(string.ascii_lowercase)
input_index     = list(range(1, 26 + 1))

for _seq in range(_input_length):
    _i = input_character.index(_input_string[_seq])
    value += (input_index[_i]) * (31 ** (_seq))

print(value % 1234567891)