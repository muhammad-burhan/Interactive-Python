# Guess the Number Game

import simplegui
import random
import math

guess_range = 100
rem_guess = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global rem_guess
    secret_number = random.randrange(0, 100)
    
    #taking a global var. and setting value to 100 by default
    if (guess_range == 100):
        print "New Game. Range is [0-100)"
        rem_guess = 7
    else:
        print "New Game. Range is [0-1000)"
        rem_guess = 10
        
    print "Number of remaining guesses", rem_guess
    print ""
   
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global guess_range, rem_guess
    guess_range = 100
    rem_guess = 7
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global guess_range, rem_guess
    guess_range = 1000
    rem_guess = 10
    new_game()
    
def input_guess(guess):
    #Converts and print the guess of the player
    print "Guess was", int(guess)
    global rem_guess
    #decrement each time input_guess handler called
    #also checking, subtract only if rem_guess is greater than one 
    if (rem_guess > 1):
        rem_guess -= 1
        print "Number of remaining guesses", rem_guess
    elif (rem_guess == 1):
        print "Number of remaining guesses 0"
    
    if (rem_guess >= 1):
        #comparison of secret and guessed number
        if (int(guess) == secret_number):
            print "Correct!"
            print ""
            #when correct restart again
            new_game()
        elif (int(guess) > secret_number):
            print "Lower"
        elif (int(guess) < secret_number):
            print "Higher"
        else: 
            print "Wrong input"
    else:
        #exceeded the guess limit print msg and restart
        print "You have failed this city. J.K., you lost!"
        print ""
        new_game()
        
    #Print blank line    
    print ""
    
    
# create frame
frame = simplegui.create_frame("Guess Number", 200, 200)

# register event handlers for control elements and start frame
frame.add_input("Your Guess", input_guess, 200)
frame.add_button("Range [0-100)",range100, 200)
frame.add_button("Range [0-1000)", range1000, 200)
frame.add_button ("Restart", new_game, 200)

# call new_game 
new_game()

