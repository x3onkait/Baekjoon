trials = int(input())

for _seq in range(trials):
    school_list = []
    drink_list  = []
    for _schools in range(int(input())):
        school, drink = input().split()
        school_list.append(school)
        drink_list.append(int(drink))

    print(school_list[drink_list.index(max(drink_list))])