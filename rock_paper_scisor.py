"""This is a rock-paper-scissors style game which pits the user against the computer in the game we all know."""

from random import randint
from time import sleep

options = ["R", "P", "S"]

lose_message = "Sorry, better luck next time!"
win_message = "Your the winner!"

def decide_winner(user_choice, computer_choice):
  print "So your choice is %s" % (user_choice)
  print "Computer selecting...."
  sleep(1)
  print "The ccomputer chose: %s" % (computer_choice)
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  
  if user_choice_index == computer_choice_index:
    print "Its a tie!"
    
  elif user_choice_index == 0 and computer_choice_index == 2:
    print win_message
    
  elif user_choice_index == 1 and computer_choice_index == 0:
    print win_message
    
  elif user_choice_index == 2 and computer_choice_index == 1:
    print win_message
    
	elif user_choice_index > 2:
    print "Thats not an option..."
    return
  
  else:
    print lose_message
    
def play_RPS():
  print "The name of the game is Rock, Paper, Scissors: and unless you have lived under a rock your whole life, you have played it so you know the rules."
  user_choice = raw_input("Make your chocie: Select R for Rock, P for Paper, or S for Scissors: ")
  sleep(1)
  user_choice.uppercase()
  computer_choice = options[randint(0, len(options)-1)]
  
decide_winner(user_choice, computer_choice)

play_RPS()