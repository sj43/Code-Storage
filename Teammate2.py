from collections import Counter
import math


def getpair(A, C):
    answer = 1
    while len(A) > 2:
        if len(A) == 4 and A[0] == A[1] == A[2] == A[3]:
            count = C[A.pop()]
            answer *= (count * (count - 1) / 2) / 2
            break
        max_f = A.pop()
        max_s = A.pop()
        count = int(C[max_s])
        if max_f == max_s:
            answer *= (count * (count - 1) / 2)
            C[max_f] -= 2
        else:
            answer *= count
            C[max_f] -= 1
            C[max_s] -= 1
    print(int(answer) % 1000000007)


t = int(input())
for i in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    C = Counter(A)
    getpair(A, C)

    # if len(A) <= 2:
    #     return 1
    # result = 1
    # while A:
    #     max_f = A.pop()
    #     max_s = A.pop()
    #     C[max_f] -= 1
    #     count = int(C[max_s])
    #     C[max_s] -= 1
    #     result *= count
    # return result % 1000000007
