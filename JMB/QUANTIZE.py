INF = 987654321

def precalc():
    A.sort()
    pSum.append(A[0])
    pSqSum.append(A[0]*A[0])
    for i in xrange(1, N):
        pSum.append(pSum[i-1] + A[i])
        pSqSum.append(pSqSum[i-1] + A[i]*A[i])


def minError(lo, hi):
    sum_ = pSum[hi] - (0 if lo == 0 else pSum[lo-1])
    sqSum = pSqSum[hi] - (0 if lo == 0 else pSqSum[lo-1])
    m = int(0.5 + float(sum_)/(hi-lo+1))
    ret = sqSum - 2*m*sum_ + m*m*(hi-lo+1)
    return ret


def quantize(from_, parts):
    if from_ == N:
        return 0
    if parts == 0:
        return INF

    if (from_, parts) in cache:
        return cache[(from_, parts)]
    ret = INF
    partSize = 1
    while from_ + partSize <= N:
        ret = min(ret, minError(from_, from_ + partSize - 1) + quantize(from_ + partSize, parts - 1))
        partSize += 1
    cache[(from_, parts)] = ret
    return ret


C = input()
for _ in xrange(C):
    N, S = map(int, raw_input().strip().split())
    A = map(int, raw_input().strip().split())
    pSum = []
    pSqSum = []
    cache = {}
    precalc()
    print quantize(0, S)
