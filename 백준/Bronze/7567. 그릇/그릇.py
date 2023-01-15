plates = list(input())

length = 10
for _seq in range(1, len(plates) + 1):

    try:
        if plates[_seq] == plates[_seq - 1]:
            length += 5
        else:
            length += 10
    except IndexError:
        break

print(length)