def length(head):
    if not head:
        return 0
    return 1 + length(head.next)

def intersection(a, b):
    m, n = length(a), length(b)
    cur_a, cur_b = a, b

    if m > n:
        for _ in xrange(m - n):
            cur_a = cur_a.next
    else:
        for _ in xrange(n - m):
            cur_b = cur_b.next

    while cur_a != cur_b:
        cur_a = cur_a.next
        cur_b = cur_b.next

    return cur_a 
