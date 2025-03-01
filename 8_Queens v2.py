import random


def amniat(board, row, column):
    for i in range(column):  # برای برسی ستون ها
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):  # برای برسی امنیت قطر اصلی ماتریس
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(column, -1, -1)):  # برای برسی امنیت قطر فرعی ماتریس
        if board[i][j] == 1:
            return False

    return True


def solve(board, column):
    if column >= len(board):
        return True
    rows = list(range(len(board)))
    random.shuffle(rows)
    for i in rows:
        if amniat(board, i, column):
            board[i][column] = 1
            if solve(board, column + 1):
                return True
            board[i][column] = 0

    return False


while True:
    def printer(board):
        for row in board:
            print(" ".join("V" if x == 1 else "-" for x in row))


    def group():
        n = int(input("pls enter the number of queens: "))
        board = [[0] * n for _ in range(n)]

        if solve(board, 0):
            printer(board)
        else:
            print("No solution")

    group()

