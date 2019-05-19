def two_sum(arr, k):
    d = {}

    for a in arr:
        if a in d:
            return True
        d[k-a] = True

    return False


ex1 = [10, 15, 3, 7]
print two_sum(ex1, 17)

ex2 = [1, 2, 3, 4, 5, 6, 7]
print two_sum(ex2, 12) 
