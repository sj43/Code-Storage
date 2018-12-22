from collections import defaultdict


def shortest_path(path, visited, cur_length):

    if len(path) == N:
        return cur_length

    ret = float('inf')

    for next_city in xrange(N):
        
        if visited[next_city]:
            continue

        cur_city = path[-1]
        path.append(next_city)
        visited[next_city] = True
        
        candidate = shortest_path(path, visited, cur_length + dist[cur_city][next_city])
        ret = min(ret, candidate)
        visited[next_city] = False
        path.pop()
        
    return ret



for _ in xrange(input()):

    N = int(input())
    dist = []

    for _ in xrange(N):
        dist.append(list(map(float, raw_input().strip().split())))

    cand = float('inf')

    for city in xrange(N):
        path = [city]
        visited = defaultdict(bool)
        visited[city] = True
        cand = min(cand, shortest_path(path, visited, 0.0))

    print cand
    
