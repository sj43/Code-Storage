


from bisect import bisect_left

lst = list(map(int, input().split()))
K = int(input())

# O(nlogn) time , O(1) space solution
# iterate and binary search through list

def two_sum(lst, K):
    lst.sort()
    for i in range(len(lst)):
        target = K - lst[i]
        j = binary_search(lst, target)
        if j == -1:
            continue
        elif j != i:
            return True
        elif j + 1 < len(lst) and lst[j + 1] == target:
            return True
        elif j - 1 >= 0 and lst[j - 1] == target:
            return True
    return False


def binary_search(lst, target):
    lo = 0
    hi = len(lst)
    ind = bisect_left(lst, target, lo, hi)
    if 0 <= ind < hi and lst[ind] == target:
        return ind
    return -1
