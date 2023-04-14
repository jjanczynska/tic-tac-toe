import random 
from os import system, name
import time
import colorama
from colorama import Fore, Back

colorama.init(autoreset=True)


def clear():
    """
    Clear the screen
    """
    _ = system("cls" if name == "nt" else "clear")


def to_center(logo, width):
    """
    Manual centering of logo
    """
    padding = ' '*(width//2)
    parts = [padding[0: (width-len(p))//2+1]+p for p in logo]
    return '\n'.join(parts)


def print_center(content, width):
    """
    Manual centering of board
    """
    padding = ' '*(width//2)
    parts = [padding[0: (width-len(p))//2+1]+p for p in content]
    return '\n'.join(parts)


def rules_of_the_game():
    """
    Explains how the game is played
    """
    print(Fore.YELLOW + 'TIC TAC TOE'.center(80))
    print(Fore.YELLOW + 'Game is played on a grid 3x3 squares'.center(80))
    print(Fore.GREEN + ' 1 | 2 | 3'.center(80))
    print(Fore.GREEN + '---|---|---'.center(80))
    print(Fore.GREEN + ' 4 | 5 | 6'.center(80))
    print(Fore.GREEN + '---|---|---'.center(80))
    print(Fore.GREEN + ' 7 | 8 | 9'.center(80))
    print(Fore.YELLOW + 'You are X, computer is O.'.center(80))
    print(Fore.YELLOW + 'Players take turns putting'.center(80))
    print(Fore.YELLOW + 'Marks in empty squares on the board'.center(80))
    print(Fore.YELLOW + 'First player to get 3 marks in a row -'.center(80))
    print(Fore.YELLOW + 'UP, DOWN, ACROSS, DIAGONALLY- '.center(80))
    print(Fore.YELLOW + 'is the WINNER.'.center(80))
    print(Fore.YELLOW + 'When all 9 squares are full-'.center(80))
    print(Fore.YELLOW + 'the GAME IS OVER!'.center(80))


def print_game_logo():
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
    clear()
    print(Fore.GREEN + to_center(logo.splitlines(), 80))


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


def print_board_centered(board):
    """
    Function takes tick tack toe board as an argument
    Prints it in a readable format
    """
    board_content = [' |  |',
                     '  ' + board[1]+'| ' + board[2]+'| ' + board[3],
                     ' |  |',
                     '------------',
                     ' |  |',
                     '  ' + board[4]+'| ' + board[5]+'| ' + board[6],
                     ' |  |',
                     '------------',
                     ' |  |',
                     '  ' + board[7]+'| ' + board[8]+'| ' + board[9],
                     ' |  |']

    centered_board = to_center(board_content, 80)
    print(centered_board)


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
        position = input(Fore.BLUE + 'Select a position to place an \'X\':')
        try:
            position = int(position)
            if position < 1 or position > 9:
                print(Fore.RED+'Enter a number between 1 and 9'.center(80))
            elif not is_space_free(board, position):
                print(Fore.RED + 'Space is occupied!'.center(80))
            else:
                return position
        except ValueError:
            print(Fore.RED + 'Please type a number!'.center(80))


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

    for i in range(1, 10):
        board_copy = board.copy()
        if is_space_free(board_copy, i):
            insert_lett(board_copy, 'XO'[computer_lett == 'O'], i)
            if is_winner(board_copy, 'XO'[computer_lett == 'O']):
                return i

    # If no winning move is possible, return a random move
    possible_moves = [i for i in range(1, 10) if is_space_free(board, i)]
    if possible_moves:
        return random.choice(possible_moves)

    # If there are no possible moves, return None (or raise an exception)
    return None


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
    print_game_logo()
    time.sleep(3)
    clear()
    rules_of_the_game()
    time.sleep(4)
    board = create_board()
    print(Fore.YELLOW + 'Tic-Tac-Toe - Welcome to the game!'.center(80))
    print_board_centered(board)

    while not is_board_full(board):
        if not is_winner(board, 'O'):
            position = get_player_move(board)
            insert_lett(board, 'X', position)
            print_board_centered(board)
        else:
            print(Fore.RED + 'Sorry, your opponent won this game!'.center(80))
            break

        if not is_winner(board, 'X'):
            position = get_computer_move(board, 'O')
            if position == 0:
                break
            insert_lett(board, 'O', position)
            print(Fore.CYAN + "Computer placed 'O' on:", position)
            print_board_centered(board)
        else:
            print(Fore.GREEN + '"X" won the game!'.center(80))
            break

        if is_board_full(board) and not is_winner(board, "X") \
                and not is_winner(board, "O"):
            print(Fore.YELLOW + 'This game is a Tie!'.center(80))

    while True:
        answer = input('Would you like to play again? (Y/N)'.center(80))
        if answer.lower() == 'y' or answer.lower() == 'yes':
            board = create_board()
            print('--------------------------------------')
            main_game()
        else:
            break


if __name__ == '__main__':
    main_game()
