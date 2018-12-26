def reverse(index):
    if quadtree[index] == 'b' or quadtree[index] == 'w':
        return (quadtree[index], index + 1)

    index += 1

    upper_left, index = reverse(index)
    upper_right, index = reverse(index)
    lower_left, index = reverse(index)
    lower_right, index = reverse(index)

    return 'x' + lower_left + lower_right + upper_left + upper_right, index


for _ in xrange(input()):
    quadtree = raw_input().strip()
    reversed_quadtree, _ = reverse(0)
    print reversed_quadtree

    
