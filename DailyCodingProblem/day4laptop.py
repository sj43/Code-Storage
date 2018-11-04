def day4naive(lst):
    lst.sort()
    missing_minimum = 1
    for elem in lst:
        if elem > 0 and elem == missing_minimum:
            missing_minimum += 1
    return missing_minimum

lst = list(map(int, input().split()))
print(day4naive(lst))
