_first          = input()
_operator       = input()
_second         = input()

_len_first      = len(_first.replace('1', ''))
_len_second     = len(_second.replace('1', ''))

if _operator == "*":
    print(f"1{'0' * (_len_first + _len_second)}")
elif _operator == "+":
    if _len_first > _len_second:
        print(f"1{'0' * (_len_first - _len_second - 1)}1{'0' * (_len_second)}")
    elif _len_second > _len_first:
        print(f"1{'0' * (_len_second - _len_first - 1)}1{'0' * (_len_first)}")
    else:   # same
        print(f"2{'0' * (_len_second)}")