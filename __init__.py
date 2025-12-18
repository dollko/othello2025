# ===============================
# myai（AI本体）を定義
# ===============================

import random

EMPTY = 0
BLACK = 1
WHITE = -1

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]

def is_valid_move(board, r, c, color):
    if board[r][c] != EMPTY:
        return False

    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        found_opponent = False

        while 0 <= nr < 8 and 0 <= nc < 8:
            if board[nr][nc] == -color:
                found_opponent = True
            elif board[nr][nc] == color:
                if found_opponent:
                    return True
                break
            else:
                break
            nr += dr
            nc += dc

    return False

def get_valid_moves(board, color):
    moves = []
    for r in range(8):
        for c in range(8):
            if is_valid_move(board, r, c, color):
                moves.append((r, c))
    return moves

# ===============================
# ★ play() に渡す AI 関数
# ===============================
def myai(board, color):
    """
    board : 8x8 二次元リスト
    color : 1 (黒) or -1 (白)
    return: (row, col) or None
    """
    moves = get_valid_moves(board, color)
    if not moves:
        return None      # パス
    return random.choice(moves)

# ===============================
# 実行
# ===============================
from sakura import othello
othello.play(myai)

