# create an empty board to play the game
def create_board():
    board = ["" for i in range(10)]
    return board

# place a letter on the board
def insert_letter(board, letter, position):
    board[position] = letter


# check if the space on the board is free
def check_if_space_free(board, position):
    return board[position]==""


# print the current board
def print_board(board):
    print("   |  |")
    print("  " + board[1]+" | " + board[2]+" | " + board[3])
    print("   |  |")
    print("------------")
    print("   |  |")
    print("  " + board[4]+" | " + board[5]+" | " + board[6])
    print("   |  |")
    print("------------")
    print("   |  |")
    print("  " + board[7]+" | " + board[8]+" | " + board[9])
    print("   |  |")


board = create_board()
print_board(board)


# check if the player or the computer has won
def is_winner(board, letter):
    return ((board[7] == letter & board[8] == letter & board[9] == letter) |
            (board[4] == letter & board[5] == letter & board[6] == letter) |
            (board[1] == letter & board[2] == letter & board[3] == letter) |
            (board[1] == letter & board[4] == letter & board[7] == letter) |
            (board[2] == letter & board[5] == letter & board[8] == letter) |
            (board[3] == letter & board[6] == letter & board[9] == letter) |
            (board[1] == letter & board[5] == letter & board[9] == letter) |
            (board[3] == letter & board[5] == letter & board[7] == letter))


# get the players move
#def get_player_move():

# get the computers move
#def get_computer_move():

# check if the board is full
#def is_board_full():


