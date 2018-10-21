from collections import Counter


def getpair(A, C):
    if len(A) <= 2:
        return 1
    result = 1
    while A:
        max_f = A.pop()
        max_s = A.pop()
        C[max_f] -= 1
        count = int(C[max_s])
        C[max_s] -= 1
        result *= count
    return result % 1000000007


t = int(input())
for i in range(t):
    n = int(input())
    A = list(map(int, input().split(" ")))
    A.sort()
    C = Counter(A)
    print(getpair(A, C))
