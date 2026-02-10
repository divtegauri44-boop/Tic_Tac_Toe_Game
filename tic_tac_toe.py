

board = [" " for _ in range(9)]

def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(player):
    win_conditions = [
        (0,1,2),(3,4,5),(6,7,8),  # rows
        (0,3,6),(1,4,7),(2,5,8),  # columns
        (0,4,8),(2,4,6)           # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_conditions)

def is_draw():
    return " " not in board

def play_game():
    current_player = "X"
    print("Tic Tac Toe Game")
    print("Positions are from 1 to 9 as shown below:")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")

    while True:
        print_board()
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

        if board[move] != " ":
            print("❌ That position is already taken. Try again.")
            continue

        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins!")
            break

        if is_draw():
            print_board()
            print("🤝 It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()
