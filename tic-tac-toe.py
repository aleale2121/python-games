from __future__ import print_function

# Constants
EMPTY = '_'
SPACE = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'
BOARD_SIZE = 9

# Initialize the board
board = [EMPTY] * 6 + [SPACE] * 3

# Mapping of moves to board indices
move_to_index = {
    'a1': 0, 'b1': 1, 'c1': 2,
    'a2': 3, 'b2': 4, 'c2': 5,
    'a3': 6, 'b3': 7, 'c3': 8
}

# Winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

def print_board():
    """Prints the current state of the board."""
    print('   a   b   c')
    print(f'1 _{board[0]}_|_{board[1]}_|_{board[2]}_')
    print(f'2 _{board[3]}_|_{board[4]}_|_{board[5]}_')
    print(f'3  {board[6]} | {board[7]} | {board[8]}')

def is_valid_move(move):
    """Checks if the move is valid."""
    return move in move_to_index and board[move_to_index[move]] in (EMPTY, SPACE)

def make_move(move, player):
    """Updates the board with the player's move."""
    board[move_to_index[move]] = player

def check_winner(player):
    """Checks if the player has won."""
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_board_full():
    """Checks if the board is full."""
    return all(cell != EMPTY and cell != SPACE for cell in board)

def reset_board():
    """Resets the board to its initial state."""
    global board
    board = [EMPTY] * 6 + [SPACE] * 3

def player_turn(player):
    """Handles a player's turn."""
    print_board()
    move = input(f'Player {player}, enter the space you want (e.g., a1): ').strip().lower()
    if is_valid_move(move):
        make_move(move, player)
        if check_winner(player):
            print_board()
            print(f'Winner is {player}!')
            play_again()
        elif is_board_full():
            print_board()
            print('This game is a draw.')
            play_again()
        else:
            player_turn(PLAYER_O if player == PLAYER_X else PLAYER_X)
    else:
        print('Error: Invalid move. Please try again.')
        player_turn(player)

def play_again():
    """Asks the players if they want to play again."""
    choice = input('Would you like to play again? Enter Y or N: ').strip().upper()
    if choice == 'Y':
        reset_board()
        start_game()
    elif choice == 'N':
        print('Thanks for playing!')
        exit()
    else:
        print('Invalid choice. Please enter Y or N.')
        play_again()

def start_game():
    """Starts the game."""
    first_player = input('Who will go first? (X or O): ').strip().upper()
    if first_player in (PLAYER_X, PLAYER_O):
        player_turn(first_player)
    else:
        print('Invalid choice. Please enter X or O.')
        start_game()

# Start the game
start_game()