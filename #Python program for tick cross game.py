# Define the game board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Define a function to print the game board
def print_board(board):
    print("   1   2   3 ")
    print("1: " + " | ".join(board[0]))
    print("  ---|---|---")
    print("2: " + " | ".join(board[1]))
    print("  ---|---|---")
    print("3: " + " | ".join(board[2]))

# Define a function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in board:
        if row == [player, player, player]:
            return True

    # Check columns
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    # No win found
    return False

# Define a function to check if the game is a tie
def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

# Define a function to get the next move from the player
def get_move(player):
    print(f"Player {player}'s turn:")
    valid_move = False
    while not valid_move:
        row = int(input("Enter the row number (1-3): ")) - 1
        column = int(input("Enter the column number (1-3): ")) - 1
        if board[row][column] == " ":
            valid_move = True
        else:
            print("Invalid move. That space is already taken.")
    return row, column

# Define the main game loop
def play_game():
    print("Welcome to Tick Cross Game")
    print_board(board)
    current_player = "X"
    while True:
        row, column = get_move(current_player)
        board[row][column] = current_player
        print_board(board)
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if check_tie(board):
            print("The game is a tie.")
            break
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

# Play the game
play_game()
