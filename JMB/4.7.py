def firstIndex(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1


print(firstIndex([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))
