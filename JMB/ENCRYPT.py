for _ in xrange(input()):
    string = str(raw_input().strip().split())
    string = string[2:-2]
    ans = ''
    for i in xrange(0, len(string), 2):
        ans += string[i]
    for j in xrange(1, len(string), 2):
        ans += string[j]
    print ans
