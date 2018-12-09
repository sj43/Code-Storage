from collections import deque


def naivemaxofsubarray(lst, k):
    for i in range(len(lst) - k + 1):
        print(max(lst[i:i + k]))


array = [10, 5, 2, 7, 8, 7]
k = 3
naivemaxofsubarray(array, k)


def bettermaxofsubarray(lst, k):
    q = deque()
    for i in range(k):
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)
    for i in range(k, len(lst)):
        print(lst[q[0]])
        while q and q[0] <= i - k:
            q.popleft()
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)
    print(lst[q[0]])


bettermaxofsubarray(array, k)
