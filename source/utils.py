import os


def draw_board(board):
    for i in board:
        for j in i:
            print(j, end=" ")
        print("")
    print("")


clear_screen = lambda: os.system("cls" if os.name == "nt" else "clear")


def check_winner(board) -> tuple[bool, list[list[str]]]:
    for i in range(len(board)):
        if (
            board[0][i] == board[1][i]
            and board[1][i] == board[2][i]
            and board[0][i] != "_"
        ):
            board[0][i] = "|"
            board[1][i] = "|"
            board[2][i] = "|"
            return (True, board)
        elif (
            board[i][0] == board[i][1]
            and board[i][1] == board[i][2]
            and board[i][0] != "_"
        ):
            board[i][0] = "*"
            board[i][1] = "*"
            board[i][2] = "*"
            return (True, board)
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "_":
        board[0][0] = "\\"
        board[1][1] = "\\"
        board[2][2] = "\\"
        return (True, board)
    elif (
        board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != "_"
    ):
        board[0][2] = "/"
        board[1][1] = "/"
        board[2][0] = "/"
        return (True, board)

    return (False, board)
