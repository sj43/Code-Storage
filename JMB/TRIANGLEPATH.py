def trianglepath(y, x):
    if y == n - 1:
        return triangle[y][x]
    if (y, x) in cache:
        return cache[(y, x)]
    ret = max(trianglepath(y + 1, x), trianglepath(y + 1, x + 1)) + triangle[y][x]
    cache[(y, x)] = ret
    return ret


for _ in xrange(input()):
    triangle = []
    cache = {}
    n = input()
    for _ in xrange(n):
        row = map(int, raw_input().strip().split())
        row = [element for element in row if element != ' ']
        triangle.append(row)
        
    print trianglepath(0, 0)
