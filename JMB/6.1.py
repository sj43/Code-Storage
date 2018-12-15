def sum(n):
    ret = 0
    for i in range(1, n + 1):
        ret += i
    return ret


def recursiveSum(n):
    if n == 1:
        return 1
    return n + recursiveSum(n - 1)
