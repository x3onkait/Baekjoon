def get_GCD(x, y):
    while y > 0:
        x, y = y, x % y 
    return x

def get_LCM(x, y):
    return int((x * y) / get_GCD(x, y))
    
num1, num2 = map(int, input().split())

print(get_GCD(num1, num2))
print(get_LCM(num1, num2))