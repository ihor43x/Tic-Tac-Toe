WIN_CASES = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

board = [["---------"],
         ["|", " ", " ", " ", "|"],
         ["|", " ", " ", " ", "|"],
         ["|", " ", " ", " ", "|"],
         ["---------"]]


def show_board(b):
    print(f"""---------
| {b[1][1]} {b[1][2]} {b[1][3]} |
| {b[2][1]} {b[2][2]} {b[2][3]} |
| {b[3][1]} {b[3][2]} {b[3][3]} |
---------""")


def move(player):
    while True:
        try:
            x, y = map(int, input("Enter the coordinates: ").split())
        except ValueError:
            print("You should enter numbers!")
            continue
        if not (1 <= x <= 3) or not (1 <= y <= 3):
            print("Coordinates should be from 1 to 3!")
            continue
        if board[x][y] == " ":
            board[x][y] = player
            break
        else:
            print("This cell is occupied! Choose another one!")


def get_board_sting():
    return "".join(c for line in board[1:4] for c in line[1:4])


def get_player_moves(player):
    return [i for i, n in enumerate(get_board_sting()) if n == player]


def is_winner(player):
    for case in WIN_CASES:
        if len([n for n in case if n in get_player_moves(player)]) == 3:
            return True


def is_mistake():
    if is_winner("X") and is_winner("O") or \
            abs(len(get_player_moves("X")) - len(get_player_moves("O"))) > 1:
        return True


def main():
    current_player = "X"
    show_board(board)
    while True:
        move(current_player)
        show_board(board)
        if is_mistake():
            print("Impossible")
            break
        elif is_winner(current_player):
            print(f"{current_player} wins")
            break
        elif " " not in get_board_sting():
            print("Draw")
            break
        current_player = "X" if current_player == "O" else "O"


if __name__ == '__main__':
    main()
