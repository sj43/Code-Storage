def movingAverage2(A, M):
    ret = []
    N = len(A)
    partialSum = 0
    for i in range(M - 1):
        partialSum += A[i]
    for i in range(M - 1, N):
        partialSum += A[i]
        ret.append(partialSum / M)
        partialSum -= A[i - M + 1]
    return ret
