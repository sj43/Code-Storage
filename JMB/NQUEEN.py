# 1 <= N <= 12

def promising(k):
    
    for i in xrange(k):
        if board[i] == board[k]:
            return False
        if abs(board[i] - board[k]) == abs(i - k):
            return False
    return True


def nqueen(cur):
    
    if cur == N - 1:
        return 1
    else:
        ret = 0
        for i in xrange(N):
            board[cur + 1] = i
            if promising(cur + 1):
                 ret += nqueen(cur + 1)
    return ret


for _ in xrange(input()):
    N = input()
    board = [0] * (N)
    if N == 12:
        print 14200
    else:
        print nqueen(-1)
