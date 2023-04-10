# create an empty board to play the game
def create_board():
    board = [' ' for i in range(10)]
    return board


# place a letter on the board
def insert_lett(board, lett, position):
    board[position] = lett


# check if the space on the board is free
def is_space_free(board, position):
    return board[position] == ' '


# print the current board
def print_board(board):
    print('   |  |')
    print('  ' + board[1]+' | ' + board[2]+' | ' + board[3])
    print('   |  |')
    print('------------')
    print('   |  |')
    print('  ' + board[4]+' | ' + board[5]+' | ' + board[6])
    print('   |  |')
    print('------------')
    print('   |  |')
    print('  ' + board[7]+' | ' + board[8]+' | ' + board[9])
    print('   |  |')


# check if the player or the computer has won
def is_winner(board, lett):
    return ((board[7] == lett and board[8] == lett and board[9] == lett) |
            (board[4] == lett and board[5] == lett and board[6] == lett) |
            (board[1] == lett and board[2] == lett and board[3] == lett) |
            (board[1] == lett and board[4] == lett and board[7] == lett) |
            (board[2] == lett and board[5] == lett and board[8] == lett) |
            (board[3] == lett and board[6] == lett and board[9] == lett) |
            (board[1] == lett and board[5] == lett and board[9] == lett) |
            (board[3] == lett and board[5] == lett and board[7] == lett))


# get the players position
def get_player_position(board):
    while True:
        position = input('Please select a position to place an \'X\' (1-9): ')
        try:
            position = int(position)
            if position < 1  or position > 9:
                print('Please enter a number between 1 and 9')
            elif not is_space_free(board, position):
                print('Space is occupied!')
            else:
                return position
        except ValueError:
            print('Please type a number!')


# get the computers move
def get_computer_move(board, computer_lett):
    for i in range(1, 10):
        board_copy = board.copy()
        if is_space_free(board_copy, i):
            insert_lett(board_copy, computer_lett, i)
            if is_winner(board_copy, computer_lett):
                return i
        if is_space_free(board_copy, i):
            insert_lett(board_copy, 'XO'[computer_lett == 'O'], i)
            if is_winner(board_copy, 'XO'[computer_lett == 'O']):
                return i
    for i in range(1, 10):
        if is_space_free(board, i):
            return i


# check if the board is full
def is_board_full(board):
    return all(space == ' ' for space in board)


def main_game():
    board = create_board()
    print('Tic-Tac-Toe - Welcome to the game!')
    print_board(board)

    while not is_board_full(board):
        if not is_winner(board, 'O'):
            position = get_player_position(board)
            insert_lett(board, 'X', position)
            print_board(board)
        else:
            print('Sorry, your opponent won this game!')
            break

        if not is_winner(board, 'X'):
            position = get_computer_move(board, 'O')
            if position == 0:
                print('This game is a Tie!')
            else:
                insert_lett(board, 'O', position)
                print("Computer placed an 'O' in position:", position)
                print_board(board)
        else:
            print('"X" won the game!')
            break

        if is_board_full(board) and not (is_winner(board, 'X')) \
                and not is_winner(board, 'O'):
            print('This game is a Tie!')

    while True:
        answer = input('Would you like to play another round? (Y/N)')
        if answer.lower() == 'y' or answer.lower() == 'yes':
            board = create_board()
            print('--------------------------------------')
            main_game()
        else:
            break
