# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
# Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

lst1 = [2, 4, 6, 2, 5]
lst2 = [5, 1, 1, 5]
lst3 = [1, 20, 3]


# this runs in O(N) time and O(N) space.
def largest_sum_nonadjacent(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) <= 2:
        return max(0, max(lst))
    d = {}
    len_lst = len(lst)
    d[0] = lst[0]
    d[1] = max(lst[0], lst[1])
    for i in range(2, len_lst):
        d[i] = max(d[i - 1], d[i - 2] + lst[i])
    return d[len_lst - 1]


print(largest_sum_nonadjacent(lst1))
print(largest_sum_nonadjacent(lst2))
print(largest_sum_nonadjacent(lst3))

# notice we only make use of last two elements in memoizaion d. Thus, why don't we just make them variables?
# this runs in O(N) time and constance space
def largest_non_adjacent(arr):
    if len(arr) <= 2:
        return max(0, max(arr))

    max_excluding_last = max(0, arr[0])
    max_including_last = max(max_excluding_last, arr[1])

    for num in arr[2:]:
        prev_max_including_last = max_including_last

        max_including_last = max(max_including_last, max_excluding_last + num)
        max_excluding_last = prev_max_including_last

    return max(max_including_last, max_excluding_last)
