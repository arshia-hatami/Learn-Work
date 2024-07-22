def aminiat(board, row, column):
    for i in range(column):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), (column, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), (column, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def printer(board):
    for row in board:
        print(" ".join("V" if x == 1 else "*" for x in row))


def group():
    while True:
        n = int(input("Enter board size:"))
        print("-" * 40)
        v = int(input("Enter the number of Queens:"))
        print("-" * 40)
        board = [[0] * n for _ in range(n)]

        for i in range(v):
            row = int(input(f"enter a row for queen num {i + 1} (0 to {n - 1})"))
            column = int(input(f"enter a column for queen num {i + 1} (0 to {n - 1})"))
            if row < 0 or row >= n or column < 0 or column >= n:
                print("Invalid")
                return
            board[row][column] = 1
            printer(board)
            board[row][column] = 0

        all_safe = True
        for i in range(v):
            row = int(input(f"enter a row for queen num {i + 1} again !"))
            column = int(input(f"enter a column for queen num {i + 1} again !"))
            if not aminiat(board, row, column):
                all_safe = False
                break
            board[row][column] = 1

        if all_safe:
            printer("all positions confirmed !")
        else:
            print("invalid positioning !")

        continue_ = input("Try again ? (y/n)").strip().lower()
        if continue_ != "y":
            break


group()
