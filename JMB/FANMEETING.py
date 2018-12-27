def hugs(members, fans):
    n = len(members)
    m = len(fans)

    a = [0] * n
    for i in xrange(n):
        if members[i] == 'M':
            a[i] = 1

    b = [0] * m
    for i in xrange(m):
        if fans[i] == 'M':
            b[m - i - 1] = 1

    c = karatsuba(a, b)
    all_hugs = 0

    for i in xrange(n - 1, m):
        if c[i] == 0:
            all_hugs += 1

    return all_hugs


def karatsuba(a, b):
    n = len(b)
    m = len(a)

    # if b is longer than a, run karatsuba the other way.
    if m < n:
        return karatsuba(b, a)

    if m == 0 or n == 0:
        return []

    # use normal multiplication if a is small.
    if m <= 50:
        return multiply(a, b)

    half = m / 2

    # set a0, a1, b0, b1.
    a0 = a[:half]
    a1 = a[half:]
    b0 = b[:min(n, half)]
    b1 = b[min(n, half):]

    # z2 = a1 * b1
    z2 = karatsuba(a1, b1)

    # z0 = a0 * b0
    z0 = karatsuba(a0, b0)

    # merge a0 and a1 all together to a0.
    addTo(a0, a1, 0)
    
    # merge b0 and b1 all together to b0.
    addTo(b0, b1, 0)

    # z1 = (a0 * b0) - z0 - z2
    z1 = karatsuba(a0, b0)
    subFrom(z1, z0)
    subFrom(z1, z2)

    # ret = z0 + z1 * 10 ^ half + z2 * 10 ^ (half * 2)
    ret = []
    addTo(ret, z0, 0)
    addTo(ret, z1, half)
    addTo(ret, z2, half + half)

    return ret


def addTo(a, b, k):
    n = len(b)
    m = len(a)
    
    if n + k > m:
        diff = n + k - m
        for _ in xrange(diff):
            a.append(0)

    for i in xrange(n):
        a[i + k] += b[i]


def subFrom(a, b):
    n = len(b)
    m = len(a)

    if n > m:
        diff = n - m
        for _ in xrange(diff):
            a.append(0)

    for i in xrange(n):
        a[i] -= b[i]


def multiply(a, b):
    n = len(b)
    m = len(a)

    c = [0] * (m + n + 1)

    for i in xrange(m):
        for j in xrange(n):
            c[i + j] += a[i] * b[j]

    return c


for _ in xrange(input()):
    members = raw_input().strip()
    fans = raw_input().strip()
    print hugs(members, fans)
