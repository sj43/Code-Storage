def next_higher_number_with_same_bits(x):
    next = 0
    if x:
        r = x & -(x)
        next_higher_number_bit = x + int(r)
        rp = x ^ int(next_higher_number_bit)
        rp = (int(rp) / int(r))
        rp = int(rp) >> 2
        next = next_higher_number_bit | rp
    return next


def chefadd2(a, b, c):
    cnt = 0
    a_count = bin(a).count("1")
    b_count = bin(b).count("1")
    a = 2**(a_count) - 1
    while True:
        if a > c:
            break
        cur_b = c - a
        if bin(cur_b).count("1") == b_count:
            cnt += 1
        a = next_higher_number_with_same_bits(a)
    return cnt


t = int(input())
for i in range(t):
    A, B, C = list(map(int, input().split(" ")))
    print(chefadd2(A, B, C))
