def pick(n, picked, toPick):
    if toPick == 0:
        print(picked)
        return
    smallest = 0 if picked == [] else picked[-1] + 1
    for next in range(smallest, n):
        picked.append(next)
        pick(n, picked, toPick - 1)
        picked.pop()


lst = []
pick(10, lst, 4)
