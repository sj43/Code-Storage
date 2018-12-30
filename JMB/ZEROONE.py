lst = str(raw_input().strip().split())
for _ in xrange(input()):
    a, b = map(int, raw_input().strip().split())
    if a > b:
        a, b = b, a
    same = True
    first = lst[a]
    for i in xrange(a + 1, b + 1):
        if lst[i] != first:
            same = False
            break
    if same:
        print 'Yes'
    else:
        print 'No'
