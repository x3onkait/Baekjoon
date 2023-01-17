games = int(input())

for _games in range(games):

    Yonsei = Korea = 0

    for _seq in range(9):
        Yonsei_play, Korea_play = map(int, input().split())
        Yonsei += Yonsei_play
        Korea  += Korea_play

    print("Yonsei") if Yonsei > Korea else print("Korea") if Yonsei < Korea else print("Draw")