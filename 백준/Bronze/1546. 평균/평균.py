input()     # ignore

current_scores  = list(map(int, input().split()))
modified_scores = list(map(lambda x: (x / max(current_scores)) * 100, current_scores))

print(sum(modified_scores) / len(modified_scores))