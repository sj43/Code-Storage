from collections import deque


dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def worms():
    ret = 0
    for y in xrange(0, N):
        for x in xrange(0, M):
            ret += bfs(y, x)
    return ret


def bfs(start_y, start_x):
    if land[start_y][start_x] == 0:
        return 0

    if (start_y, start_x) in visited:
        return 0

    Q = deque()


    visited[(start_y, start_x)] = True

    Q.append((start_y, start_x))

    while(len(Q) != 0):
        cur_y, cur_x = Q.popleft()
        for i in xrange(4):
            moveto_y = cur_y + dy[i]
            moveto_x = cur_x + dx[i]
            if moveto_y >= 0 and moveto_y < N and moveto_x >= 0 and moveto_x < M:
                if (moveto_y, moveto_x) in visited:
                    continue
                visited[(moveto_y, moveto_x)] = True
                if land[moveto_y][moveto_x] != 0:
                    Q.append((moveto_y, moveto_x))

    return 1



C = input()
for _ in xrange(C):
    M, N, K = map(int, raw_input().strip().split())
    land = [[0 for i in xrange(M)] for j in xrange(N)]
    visited = {}
    for _ in xrange(K):
        X, Y = map(int, raw_input().strip().split())
        land[Y][X] = 1
    print worms()
