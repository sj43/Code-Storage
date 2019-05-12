def non_overlapping_intervals(arr):
    cur_end = float('-inf')
    overlapping = 0

    for s, e in sorted(arr, key = lambda x : x[1]):
        if s > cur_end:
            cur_end = e
        else:
            overlapping += 1

    return overlapping


example = [(7,9),(2,4),(5,8)]
print non_overlapping_intervals(example)
