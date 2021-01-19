# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# required modules
import math
import random
import simplegui

game_data = {
    "guess_point_left": 0,
    "guess_range": 100,
    "secret": 0
  }

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global game_data
    game_data['guess_point_left'] = int(math.ceil(math.log((game_data['guess_range'] - 0), 2)))
    game_data['secret'] = random.randrange(0, game_data['guess_range'])
    print "\nNew game. Range is from 0 to", game_data['guess_range']
    print "Number of remaining guesses is", game_data['guess_point_left']


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global game_data
    game_data['guess_range'] = 100
    # remove this when you add your code    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global game_data
    game_data['guess_range'] = 1000
    new_game()
    
def input_guess(guess):
    global game_data
    print "\nGuess was", guess
    guess = int(guess)
    game_data['guess_point_left'] -= 1
    print "Number of remaining guesses is", game_data['guess_point_left']
    # main game logic goes here
    if game_data['guess_point_left'] > 0:
        if guess > game_data['secret']:
            print "Lower"
        elif guess < game_data['secret']:
            print "Higher"
        else:
            print "Correct"
            new_game()
    else:
        if guess == game_data['secret']:
            print "Correct"
        else:
            print "You ran out of guesses. The number was", game_data['secret']
        new_game()
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess:", input_guess, 200)

# call new_game 
new_game()
