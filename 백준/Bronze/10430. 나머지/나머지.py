data = input()

A, B, C = int(data.split(' ')[0]), int(data.split(' ')[1]), int(data.split(' ')[2])

v1 = (A+B)%C
v2 = ((A%C) + (B%C))%C
v3 = (A*B)%C
v4 = ((A%C) * (B%C))%C

print(v1)
print(v2)
print(v3)
print(v4)