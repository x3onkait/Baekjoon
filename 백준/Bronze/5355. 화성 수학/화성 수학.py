_qty    = int(input())
_output = ""

for _seq in range(_qty):

    expression = input().split(' ')
    result = 0.0

    for _operation in expression:

        if _operation == "@":
            result *= 3
        elif _operation == "%":
            result += 5
        elif _operation == "#":
            result -= 7
        else:
            result += float(_operation)

    _output += f"{result:.2f}\n"

print(_output)