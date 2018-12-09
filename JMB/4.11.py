MIN = float('-inf')

def fastestMaxSum(A):
    N = len(A)
    ret = MIN
    psum = 0
    for i in range(N):
        psum = max(0, psum) + A[i]
        ret = max(psum, ret)
    return ret


print(fastestMaxSum([-7, 4, -3, 6, 3, -8, 3, 4]))
