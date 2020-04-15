###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random


def generate_code():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def get_guess():
    return list(input("What is your guess?"))

def get_clues(user_guess,secretCode):

    if user_guess == secretCode:
        return ["Code Cracked"]
    clues = []
    for i,num in enumerate(user_guess):
        if num == secretCode[i]:
            print("A")
            clues.append("Match")
        elif num in secretCode:
            clues.append("Close")
    if clues == []:
        return ["Nope"]
    else:
        return clues


# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!

print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")

# Create a Secret Code to start the Game
secretCode = generate_code()
print("Code has been generated, please guess a 3 digit number")

clues = []

while True:
    user_guess = get_guess()
    print(user_guess)
    clues = get_clues(user_guess,secretCode)
    print("Here is the result of your guess:")
    for clue in clues:
        print(clue)

    if user_guess == secretCode:
        break