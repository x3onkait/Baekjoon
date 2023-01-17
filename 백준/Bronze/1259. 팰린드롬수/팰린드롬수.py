while True:
    number = int(input())
    if number == 0:
        break
    else:
        if str(number) == str(number)[::-1]:
            print("yes")
        else:
            print("no")