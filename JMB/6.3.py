dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]


def hasWord(y, x, word):
    if x < 0 or y < 0 or x > 4 or y > 4:
        return False
    if board[y][x] != word[0]:
        return False
    if len(word) == 1:
        return True
    for direction in range(8):
        nextY = y + dy[direction]
        nextX = x + dx[direction]
        if hasWord(nextY, nextX, word[1:]):
            return True
    return False
