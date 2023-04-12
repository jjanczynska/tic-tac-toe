import colorama
from colorama import Fore, Back

colorama.init(autoreset=True)


def game_logo():
    """
    game logo with ASCII code
    """
    logo = '''

    _|_|_|_|_|  _|_|_|    _|_|_|  
    _|        _|    _|        
    _|        _|    _|        
    _|        _|    _|        
    _|      _|_|_|    _|_|_|  

                                                      
_|_|_|_|_|    _|_|      _|_|_|  
    _|      _|    _|  _|        
    _|      _|_|_|_|  _|        
    _|      _|    _|  _|        
    _|      _|    _|    _|_|_|  
                                                            
                              
_|_|_|_|_|    _|_|    _|_|_|_|  
    _|      _|    _|  _|        
    _|      _|    _|  _|_|_|  
    _|      _|    _|  _| 
    _|        _|_|    _|_|_|_|

    '''
    print(Fore.RED + Back.BLUE + game_logo)


def create_board():
    """
    Function creates a list with 10 elements,
    Each element is put into its own space
    It returns a blank tic tac toe board
    """
    board = [' ' for i in range(10)]
    return board


def insert_lett(board, lett, position):
    """
    A letter is inserted into a position on the board
    """
    board[position] = lett


def is_space_free(board, position):
    """
    Takes the board and the position
    Checks if the specified position is empty
    """
    return board[position] == ' '


def print_board(board):
    """
    Function takes tick tack toe board as an argument
    Prints it in a readable format
    """
    print('   |  |')
    print('  ' + board[1]+'| ' + board[2]+'| ' + board[3])
    print('   |  |')
    print('------------')
    print('   |  |')
    print('  ' + board[4]+'| ' + board[5]+'| ' + board[6])
    print('   |  |')
    print('------------')
    print('   |  |')
    print('  ' + board[7]+'| ' + board[8]+'| ' + board[9])
    print('   |  |')


def is_winner(board, lett):
    """
    Takes the board and letter as an argument
    Checks if an "O" or "X" appears consecutively in a winning combo
    Returns True if the letter has won, otherwise it is false
    """
    return ((board[7] == lett and board[8] == lett and board[9] == lett) |
            (board[4] == lett and board[5] == lett and board[6] == lett) |
            (board[1] == lett and board[2] == lett and board[3] == lett) |
            (board[1] == lett and board[4] == lett and board[7] == lett) |
            (board[2] == lett and board[5] == lett and board[8] == lett) |
            (board[3] == lett and board[6] == lett and board[9] == lett) |
            (board[1] == lett and board[5] == lett and board[9] == lett) |
            (board[3] == lett and board[5] == lett and board[7] == lett))


def get_player_move(board):
    """
    Prompts the player to place "X" on the board
    Returns the position as ineger if valid
    Otherwise it asks the player to try again
    While loop is being used to ask player for a valid input
    """
    while True:
        position = input('Please select a position to place an \'X\' (1-9): ')
        try:
            position = int(position)
            if position < 1 or position > 9:
                print('Please enter a number between 1 and 9')
            elif not is_space_free(board, position):
                print('Space is occupied!')
            else:
                return position
        except ValueError:
            print('Please type a number!')


def get_computer_move(board, computer_lett):
    """
    Gets the computer to place its letter
    Checks if the computer can win the game
    by placing the letter in any of the empty spaces
    on the board, if yes, then it returns the position
    If the computer can't win, it checks if the player can
    If both can't win, it returns a random position on the board
    """

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


def is_board_full(board):
    """
    Checks if all the spaces on the board are occupied or not
    """
    for i in range(1, len(board)):
        if board[i] == ' ':
            return False

    return True


def main_game():
    """
    Runs all the game functions in a specified order
    """
    board = create_board()
    print('Tic-Tac-Toe - Welcome to the game!')
    print_board(board)

    while not is_board_full(board):
        if not is_winner(board, 'O'):
            position = get_player_move(board)
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

        if is_board_full(board) and not is_winner(board, "X") \
                and not is_winner(board, "O"):
            print('This game is a Tie!')

    while True:
        answer = input('Would you like to play another round? (Y/N)')
        if answer.lower() == 'y' or answer.lower() == 'yes':
            board = create_board()
            print('--------------------------------------')
            main_game()
        else:
            break


if __name__ == '__main__':
    main_game()
