def max_area_fence(left, right):
    if left == right:
        return fence[left]

    mid = (left + right) / 2
    
    ret = max(max_area_fence(left, mid), max_area_fence(mid + 1, right))

    lo = mid
    hi = mid + 1
    
    height = min(fence[lo], fence[hi])

    area = height * (hi - lo + 1)

    ret = max(ret, area)
    
    while left < lo or hi < right:
        if hi < right and (lo == left or fence[lo - 1] < fence[hi + 1]):
            hi += 1
            height = min(height, fence[hi])
        else:
            lo -= 1
            height = min(height, fence[lo])
        ret = max(ret, height * (hi - lo + 1))

    return ret
        

for _ in xrange(input()):
    N = input()
    fence = list(map(int, raw_input().strip().split()))
    print max_area_fence(0, len(fence) - 1)
