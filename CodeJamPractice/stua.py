def damage(P):
    i = 0
    cur_dmg = 1
    tot_dmg = 0

    while i < len(P):
        if P[i] == "S":
            tot_dmg += cur_dmg
        else:
            cur_dmg *= 2
        i += 1

    return tot_dmg


def stua(D, P):
    num_change = 0
    while True:
        if damage(P) <= D:
            return num_change
        else:
            if "CS" not in P:
                return "IMPOSSIBLE"
            else:
                k = P.rfind("CS")
                P = P[:k] + "SC" + P[k + 2:]
                num_change += 1


T = input()
for testcase in xrange(T):
    D, P = raw_input().strip().split()
    D = int(D)
    print "Case #" + str(testcase+1) + ": " + str(stua(D, P))
