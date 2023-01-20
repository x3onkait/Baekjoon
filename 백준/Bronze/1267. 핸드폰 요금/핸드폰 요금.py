N = int(input())
number_list = list(map(int, input().split()))
y = m = 0
for _seq in number_list:
    y += (_seq//30 + 1) * 10
    m += (_seq//60 + 1) * 15
if m == y:
    print(f"Y M {m}")
elif m < y:
    print(f"M {m}")
else:
    print(f"Y {y}")