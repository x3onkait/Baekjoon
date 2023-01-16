num1, num2 = map(int, (input().split()))
num1, num2 = int(str(num1)[::-1]), int(str(num2)[::-1])
print(max(num1, num2))