def tiling(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    if n in cache:
        return cache[n]

    ret = tiling(n - 1) % 1000000007 + tiling(n - 2) % 1000000007
    ret = ret % 1000000007
    cache[n] = ret
    return ret


C = input()
for _ in xrange(C):
    n = input()
    cache = {}
    print tiling(n)
