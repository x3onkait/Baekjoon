trial = int(input())

for _seq in range(trial):

    parenthesises = input()
    stack = []

    for _parenthesis in parenthesises:
        if _parenthesis == "(":
            stack.append(_parenthesis)
        elif _parenthesis == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    # for-else ㄴㅇㄱ
    else:
        # Did parenthesis match perfectly?
        if not stack:
            print("YES")
        else:
            print("NO")