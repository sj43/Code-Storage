n = int(input())
d = {}
for _ in range(n):
    d[_] = {}
for i in range(n):
    st = input().split()
    for s in st:
        if s in d[i]:
            d[i][s] += 1
        else:
            d[i][s] = 1
q = int(input())
for j in range(q):
    query = input().split()
    answer = []
    for k in range(n):
        isItPresent = [0] * len(query)
        for que in query:
            if que in d[k]:
                isItPresent[query.index(que)] += d[k][que]
        our_min = min(isItPresent)
        if our_min > 0:
            # if not any(v == 0 for v in isItPresent):
                answer.extend([k] * our_min)
    if answer == []:
        print(-1)
    else:
        # answer.sort
        print(*answer)
