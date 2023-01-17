nth = int(input())

# does number will include 666 or more?

trial = 0
hit   = 0

while True:

    if hit == nth:
        print(trial)
        break

    trial += 1

    if "666" in str(trial):
        hit += 1
    else:
        continue