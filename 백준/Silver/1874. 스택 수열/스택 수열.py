sequence_qty = int(input())

stack        = []
operations   = []
count        = 1
flag         = True

for _operation in range(sequence_qty):

    number = int(input())

    while count <= number:
        stack.append(count)         # The number will be inserted in ascending order like 1, 2, 3, 4, 5... even something pops out.
        operations.append("+")
        count += 1

    # in case of pop operation
    if stack[-1] == number:         # number should be same or bigger than stack[-1]
        stack.pop()
        operations.append("-")
    else:
        flag = False
        break

if flag == True:
    for _operation in operations:
        print(_operation)
else:
    print("NO")