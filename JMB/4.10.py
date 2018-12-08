MIN = float('-inf')


def fastMaxSum(A, lo, hi):
    if lo == hi:
        return A[lo]
    mid = (lo + hi) / 2
    left = MIN
    right = MIN
    sum = 0
    for i in range(mid, lo - 1, -1):
        sum += A[i]
        left = max(left, sum)
    sum = 0
    for j in range(mid + 1, hi + 1):
        sum += A[i]
        right = max(right, sum)
    single = max(fastMaxSum(A, lo, mid), fastMaxSum(A, mid + 1, hi))
    return max(left + right, single)


print(fastMaxSum([-7, 4, -3, 6, 3, -8, 3, 4], 0, 8))
