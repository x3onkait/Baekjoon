_vote_qty = int(input())
score     = 0

for _seq in range(_vote_qty):

    cast  = int(input())

    if cast == 1:
        score += 1
    else:
        score -= 1

print("Junhee is cute!") if score > 0 else print("Junhee is not cute!")