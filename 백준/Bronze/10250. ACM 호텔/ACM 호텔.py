_trial = int(input())

for _seq in range(_trial):

    height, width, guest_nth = map(int, input().split())

    room_number_height = guest_nth % height
    room_number_width = (guest_nth // height) + 1
    if room_number_height == 0:                         # exceptional cases
        room_number_height = height
        room_number_width -= 1

    print(room_number_height * 100 + room_number_width)