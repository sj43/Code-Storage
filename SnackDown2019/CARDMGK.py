T = int(input())
for _ in range(T):
    N = int(input())
    seq = list(map(int, input().strip().split()))
    splitted = False
    wrong = False
    for i in range(len(seq) - 1):
        if seq[i + 1] - seq[i] < 0:
            if (not splitted):
                if seq[0] < seq[-1]:
                    wrong = True
                    break
                else:
                    splitted = True
            else:
                wrong = True
                break
    if wrong:
        print("NO")
    else:
        print("YES")
