num1  = int(input())
num2  = int(input())
num3  = int(input())
value = num1 * num2 * num3

number_list      = list(str(value))
number_frequency = {'0' : 0, '1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0}

for _digit in number_list:
    if _digit in number_frequency:
        number_frequency[_digit] += 1
    
number_frequency = dict(sorted(number_frequency.items()))

for _value in number_frequency.values():
    print(_value)