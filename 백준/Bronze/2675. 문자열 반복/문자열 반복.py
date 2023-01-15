_qty    = int(input())
result  = ""

for _seq in range(_qty):
    
    _data   = input()
    _repeat = int(_data.split(' ')[0])
    _string = _data.split(' ')[1]

    _output = ""

    for _char in _string:
        _output += _char * _repeat

    result += f"{_output}\n"

print(result)