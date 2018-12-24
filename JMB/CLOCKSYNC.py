INF = 9999
SWITCHES = 10
CLOCKS = 16
LINKED = [
    "***.............",
    "...*...*.*.*....",
    "....*.....*...**",
    "*...****........",
    "......***.*.*...",
    "*.*...........**",
    "...*..........**",
    "....**.*......**",
    ".*****..........",
    "...***...*...*..",
]


def are_aligned(clocks):
    for clock in clocks:
        if clock != 12:
            return False
    return True


def push(clocks, switch):
    for clock in xrange(CLOCKS):
        if LINKED[switch][clock] == '*':
            clocks[clock] += 3
            if clocks[clock] == 15:
                clocks[clock] = 3


def solve(clocks, switch):
    if switch == SWITCHES:
        return 0 if are_aligned(clocks) else INF
           
    ret = INF

    for cnt in xrange(4):
        ret = min(ret, cnt + solve(clocks, switch + 1))
        push(clocks, switch)

    return ret


for _ in xrange(input()):
    clocks = map(int, raw_input().strip().split())
    ret = solve(clocks, 0)
    print ret if ret != INF else -1
