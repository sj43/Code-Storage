def selectionSort(A):
    for i in range(len(A)):
        minIndex = i
        for j in range(i + 1, len(A)):
            if A[minIndex] > A[j]:
                minIndex = j
        A[i], A[minIndex] = A[minIndex], A[i]


def insertionSort(A):
    for i in range(len(A)):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j - 1], A[j] = A[j], A[j - 1]
            j -= 1


A = [3, 1, 5, 4, 2]
selectionSort(A)
print(A)

A = [3, 1, 5, 4, 2]
insertionSort(A)
print(A)
