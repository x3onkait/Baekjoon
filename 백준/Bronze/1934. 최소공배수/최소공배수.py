def GCD(n1, n2):

    while n2 != 0:
        r = n1 % n2
        n1 = n2
        n2 = r

    return n1

def LCM(n1, n2):

    return int((n1 * n2) / GCD(n1, n2))

_qty    = int(input())
_output = ""

for _seq in range(_qty):
    n1, n2 = map(int, input().split(' '))
    _output += f"{LCM(n1, n2)}\n"

print(_output)