s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())

score = list(map(lambda x: 40 if x <= 40 else x, [s1, s2, s3, s4, s5]))

print(int(sum(score) / 5))