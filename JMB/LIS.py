
## # function lis2
##
##def lis2(start):
##    if start in cache:
##        return cache[start]
##    ret = 1
##    for cur in xrange(start + 1, N):
##        if S[start] < S[cur]:
##            ret = max(ret, 1 + lis2(cur))
##            cache[start] = ret
##
##    return ret
##
##
##    
##for _ in xrange(input()):
##    N = input()
##    cache = {}
##    S = map(int, raw_input().strip().split())
##    maxLen = 0
##    for begin in xrange(N):
##        maxLen = max(maxLen, lis2(begin))
##    print maxLen
##




### function lis3
##
##def lis3(start):
##    if start + 1 in cache:
##        return cache[start + 1]
##    ret = 1
##    for cur in xrange(start + 1, N):
##        if start == -1 or S(start) < S(cur):
##            ret = max(ret, 1 + lis3(cur))
##            cache[start + 1] = ret
##            
##    return ret
##
##
##def S(start):
##    if start == -1:
##        return float('-inf')
##    else:
##        return S_[start]
##
##    
##for _ in xrange(input()):
##    N = input()
##    cache = {}
##    S_ = map(int, raw_input().strip().split())
##    print lis3(-1) - 1






# function lis4 - binary search
def lst4(num, lis_idx):
    if lis_idx == 0 or (lis_idx > 0 and cache[lis_idx - 1] <= num):
        cache[lis_idx] = num
        lis_idx += 1
        return lis_idx

    front = 0
    rear = lis_idx - 1
    # binary search
    while front <= rear:
        mid = (front + rear) / 2
        if cache[mid] < num:
            front = mid + 1
        else:
            rear = mid - 1
    cache[rear + 1] = num
    return lis_idx


for _ in xrange(input()):
    N = input()
    cache = {}
    S = map(int, raw_input().strip().split())
    idx = 0
    for i in xrange(N):
        idx = lst4(S[i], idx)
    print idx

