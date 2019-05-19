def first_missing_positive(arr):
    if not arr:
        return 1

    for i, num in enumerate(arr):
        while i + 1 != arr[i] and 0 < arr[i] <= len(arr):
            v = arr[i]
            arr[i], arr[v - 1] = arr[v-1], arr[i]
            
    for i, num in enumerate(arr, 1):
        if i != num:
            return i

    return len(arr) + 1



ex1 = [3, 4, -1, 1] # 2
ex2 = [1, 2, 0] # 3

print first_missing_positive(ex1)
print first_missing_positive(ex2)
