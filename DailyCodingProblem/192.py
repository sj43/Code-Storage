def can_reach_end(arr):
    furthest_so_far = 0
    for i in range(len(arr)):
        if i > furthest_so_far:
            break
        furthest_so_far = max(furthest_so_far, i + arr[i])
    return furthest_so_far >= len(arr)-1


A = [1,3,1,2,0,1]
B = [1,2,1,0,0]

print can_reach_end(A)
print can_reach_end(B)
