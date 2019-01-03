from collections import defaultdict
import sys

sys.setrecursionlimit(10002)

def classify(a, b):
    M = N[a : b + 1]

    # difficulty 1 
    if M == M[0] * len(M):
        return 1

    # difficulty 2
    progressive = True
    
    for i in xrange(len(M) - 1):
        if int(M[i + 1]) - int(M[i]) != int(M[1]) - int(M[0]):
            progressive = False
            
    if progressive and abs(int(M[1]) - int(M[0])) == 1:
        return 2
    
    # difficulty 4
    alternating = True

    for i in xrange(len(M)):
        if int(M[i]) != int(M[i % 2]):
            alternating = False
            
    if alternating:
        return 4

    # difficulty 5
    if progressive:
        return 5

    # difficulty 10
    return 10


def memorize(begin):
    if begin == len(N):
        return 0
    
    if begin in cache:
        return cache[begin]

    ret = float('inf')

    # memorize(begin) = {for L from 3 to 5} min(memorize(begin + L) + classify(begin, begin + L - 1))
    for L in xrange(3, 6):
        if begin + L <= len(N):
            ret = min(ret, memorize(begin + L) + classify(begin, begin + L - 1))

    cache[begin] = ret
            
    return ret


for _ in xrange(input()):
    N = raw_input().strip() # N is a string
    cache = defaultdict(int)
    print memorize(0)
