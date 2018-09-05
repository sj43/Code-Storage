def remove_last_odd(numbers):
    rnumbers = numbers[::-1]
    for rnum in rnumbers:
        if rnum % 2 == 1:
            rnumbers.remove(rnum)
            break
    return rnumbers[::-1]


numbers = [1, 7, 3, 34, 8, 15, 7]
print(numbers)
print(remove_last_odd(numbers))
