import time
import random

# Constants
MAX_STRIKES = 6
WORD_LIST = ['acres', 'adult', 'advice', 'arrangement', 'attempt', 'August', 'Autumn', 'border', 'breeze', 'brick', 'calm', 'canal', 'Casey']
LETTERS = 'abcdefghijklmnopqrstuvwxyz'

# Game state
current_strikes = MAX_STRIKES
won_games = 0
random_word = ''
guessed_letters = set()
blanks = []

def display_hangman(strikes):
    """Displays the hangman ASCII art based on the number of strikes."""
    stages = [
        """
           ___
          |   |
          |   0
          |  /|\\
          |  / \\
         _|__________________________
        """,
        """
           ___
          |   |
          |   0
          |  /|\\
          |  /
         _|__________________________
        """,
        """
           ___
          |   |
          |   0
          |  /|\\
          |
         _|__________________________
        """,
        """
           ___
          |   |
          |   0
          |  /|
          |
         _|__________________________
        """,
        """
           ___
          |   |
          |   0
          |   |
          |
         _|__________________________
        """,
        """
           ___
          |   |
          |   0
          |
          |
         _|__________________________
        """,
        """
           ___
          |   |
          |
          |
          |
         _|__________________________
        """
    ]
    print(stages[strikes])

def display_blanks():
    """Displays the current state of the blanks (guessed letters)."""
    print(' '.join(blanks))

def reset_game():
    """Resets the game state for a new round."""
    global current_strikes, random_word, guessed_letters, blanks
    current_strikes = MAX_STRIKES
    random_word = random.choice(WORD_LIST)
    guessed_letters = set()
    blanks = ['_' for _ in random_word]

def player_guess():
    """Handles the player's guess."""
    global current_strikes, won_games

    display_blanks()
    print(f'Available letters: {LETTERS}')
    guess = input(f'You have {current_strikes} strike(s) left. Guess a letter: ').lower()

    if guess in guessed_letters:
        print('You already guessed that letter. Try again!')
        return
    elif guess not in LETTERS:
        print('Invalid input. Please enter a valid letter.')
        return

    guessed_letters.add(guess)

    if guess in random_word:
        print('Congrats! You guessed a letter!')
        for i, letter in enumerate(random_word):
            if letter == guess:
                blanks[i] = guess
    else:
        print('Sorry, that letter is not in the word. One')