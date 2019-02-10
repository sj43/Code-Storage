heap = []

def add_to_heap(x):
    heap.append(x)
    move_up(len(heap) - 1)


def remove_lowest(x):
    ret = heap[0]

    if len(heap) > 1:
        heap[0] = heap.pop()
        move_down(0)
    else:
        heap.pop()

    return ret


def move_up(i):
    while i > 0:
        p = (i - 1) // 2
        if heap[p] > heap[i]:
            heap[i], heap[p], i = heap[p], heap[i], p
        else:
            return


def move_down(i):
    I = len(heap)
    while True:
        leftc, rightc = i * 2 + 1, i * 2 + 2
        if I <= leftc:
            return
        elif I <= rightc:
            if heap[i] > heap[leftc]:
                heap[i], heap[leftc], i = heap[leftc], heap[i], leftc
            else:
                return
        else:
            target = leftc if heap[leftc] < heap[rightc] else rightc
            if heap[i] > heap[target]:
                heap[i], heap[target], i = heap[target], heap[i], target
            else:
                return



N = input()
for _ in xrange(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print 0
        else:
            print remove_lowest(x)
    else:
        add_to_heap(x)
