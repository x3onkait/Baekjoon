abbreviation = input().replace(" ","")

# BE AWARE OF THE FLOW
trigger = "UCPC"
search  = 0
flag    = False
for _seq in abbreviation:
    if _seq == trigger[search]:
        search += 1
    if search == 4:
        flag = True
        break

if flag == False:
    print("I hate UCPC")
else:
    print("I love UCPC")