def max_subarray(arr):
    max_sum_so_far = 0
    sum_now = 0
    for i in arr:
        sum_now = max(i, sum_now + i)
        max_sum_so_far = max(max_sum_so_far, sum_now)
    return max_sum_so_far



ex1 = [8,-1,3,4]
ex2 = [-4,5,1,0]
