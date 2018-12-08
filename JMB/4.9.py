MIN = float('-inf')


def inefficientMaxSum(A):
    N = len(A)
    ret = MIN
    for i in range(N):
        for j in range(i, N):
            sum = 0
            for k in range(i, j + 1):
                sum += A[k]
            ret = max(ret, sum)
    return ret


print(inefficientMaxSum([-7, 4, -3, 6, 3, -8, 3, 4]))


def betterMaxSum(A):
    N = len(A)
    ret = MIN
    for i in range(N):
        sum = 0
        for j in range(i, N):
            sum += A[j]
            ret = max(ret, sum)
    return ret


print(inefficientMaxSum([-7, 4, -3, 6, 3, -8, 3, 4]))
