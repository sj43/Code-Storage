def factor(n):
    if n == 1:
        return [1]
    ret = []
    div = 2
    while n > 1:
        while n % div == 0:
            n /= div
            ret.append(div)
        div += 1
    return ret


print(factor(6))
print(factor(10))
print(factor(20))
print(factor(100))
