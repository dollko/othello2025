# AIオセロ：エントリー関数 myai
# sakura.othello.play(myai) で動作

import random

def myai(board, color):
    moves = []

    for x in range(8):
        for y in range(8):
            if is_legal(board, color, x, y):
                moves.append((x, y))

    if not moves:
        return None

    # 角を優先
    corners = [(0,0), (0,7), (7,0), (7,7)]
    for c in corners:
        if c in moves:
            return c

    return random.choice(moves)


def is_legal(board, color, x, y):
    if board[x][y] != 0:
        return False
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx == 0 and dy == 0:
                continue
            if check(board, color, x, y, dx, dy):
                return True
    return False


def check(board, color, x, y, dx, dy):
    i, j = x + dx, y + dy
    found = False
    while 0 <= i < 8 and 0 <= j < 8:
        if board[i][j] == -color:
            found = True
        elif board[i][j] == color:
            return found
        else:
            return False
        i += dx
        j += dy
    return False

