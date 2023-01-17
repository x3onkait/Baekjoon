trials = int(input())

for _seq in range(trials):
    player_list = []
    price_list  = []
    for _player in range(int(input())):
        price, player = input().split()
        player_list.append(player)
        price_list.append(int(price))

    print(player_list[price_list.index(max(price_list))])