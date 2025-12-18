# ===============================
# Othello / Reversi Full Code
# ===============================

EMPTY = 0
BLACK = 1
WHITE = -1

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]

# ---------- 盤面初期化 ----------
def init_board():
    board = [[EMPTY]*8 for _ in range(8)]
    board[3][3] = WHITE
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[4][4] = WHITE
    return board

# ---------- 合法手判定 ----------
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
    return [(r, c) for r in range(8) for c in range(8)
            if is_valid_move(board, r, c, color)]

# ---------- 石を置く ----------
def apply_move(board, r, c, color):
    board[r][c] = color

    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        path = []

        while 0 <= nr < 8 and 0 <= nc < 8:
            if board[nr][nc] == -color:
                path.append((nr, nc))
            elif board[nr][nc] == color:
                for pr, pc in path:
                    board[pr][pc] = color
                break
            else:
                break
            nr += dr
            nc += dc

# ---------- 表示 ----------
def print_board(board):
    print("  0 1 2 3 4 5 6 7")
    for i, row in enumerate(board):
        print(i, end=" ")
        for cell in row:
            if cell == BLACK:
                print("●", end=" ")
            elif cell == WHITE:
                print("○", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

# ---------- 簡単AI（合法手からランダム） ----------
import random
def ai_random(board, color):
    moves = get_valid_moves(board, color)
    if not moves:
        return None
    return random.choice(moves)

# ---------- 人間入力 ----------
def human_player(board, color):
    moves = get_valid_moves(board, color)
    if not moves:
        return None

    print("合法手:", moves)
    while True:
        try:
            r, c = map(int, input("行 列 を入力（例: 2 3）: ").split())
            if (r, c) in moves:
                return (r, c)
        except:
            pass
        print("無効な入力です")

# ---------- ゲーム本体 ----------
def play_game(black_player, white_player):
    board = init_board()
    color = BLACK
    passes = 0

    while passes < 2:
        print_board(board)
        player = black_player if color == BLACK else white_player
        move = player(board, color)

        if move is None:
            print("パス")
            passes += 1
        else:
            apply_move(board, move[0], move[1], color)
            passes = 0

        color = -color

    # 終了
    print_board(board)
    black_count = sum(row.count(BLACK) for row in board)
    white_count = sum(row.count(WHITE) for row in board)

    print("黒:", black_count, "白:", white_count)
    if black_count > white_count:
        print("黒の勝ち")
    elif white_count > black_count:
        print("白の勝ち")
    else:
        print("引き分け")

# ===============================
# 実行例
# ===============================

# 人間 vs AI
# play_game(human_player, ai_random)

# AI vs AI
play_game(ai_random, ai_random)
