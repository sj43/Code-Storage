NEGINF = float('-inf')


def jlis(a_idx, b_idx):

    if (a_idx + 1, b_idx + 1) in cache:
        return cache[(a_idx + 1, b_idx + 1)]

    ret = 0

    a = NEGINF if a_idx == -1 else A[a_idx]
    b = NEGINF if b_idx == -1 else B[b_idx]
    
    max_element = max(a, b)

    for next_a in xrange(a_idx + 1, n):
        if max_element < A[next_a]:
            ret = max(ret, jlis(next_a, b_idx) + 1)
            
    for next_b in xrange(b_idx + 1, m):
        if max_element < B[next_b]:
            ret = max(ret, jlis(a_idx, next_b) + 1)

    cache[(a_idx + 1, b_idx + 1)] = ret

    return ret
    


for _ in xrange(input()):
    n, m = map(int, raw_input().strip().split())
    A = map(int, raw_input().strip().split())
    B = map(int, raw_input().strip().split())
    cache = {}
    print jlis(-1, -1)
