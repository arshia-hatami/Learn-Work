def amniat(board, row, column):
    for i in range(column):  # برای برسی ستون ها
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):  # برای برسی امنیت قطر اصلی ماتریس
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row - 1, len(board), 1), range(column, -1, -1)):  # برای برسی امنیت قطر فرعی ماتریس
        if board[i][j] == 1:
            return False
    return True


def solve(board, column):
    if column >= len(board):
        return True
    for i in range(len(board)):
        if amniat(board, i, column):
            board[i][column] = 1
            if solve(board, column + 1):
                return True
            board[i][column] = 0
    return False


def printer(board):
    for row in board:
        print(" ".join("V" if x == 1 else "-" for x in row))


n = 8
board = [[0] * n for i in range(n)]
if solve(board, 0):
    printer(board)
else:
    print("No solution")
