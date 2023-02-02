"""
    An implementation of Wordle (https://www.nytimes.com/games/wordle/index.html) in Python
    Filename: wordle.py
    Author: XXXXXXX XX
    Date: 17jan22
    Course: COMP1352
    Assignment: Project 2
    Collaborators: None
    Internet Source: https://canvas.du.edu/courses/159810/assignments/1280997 for colored output functions
"""

import random

# try to open word dictionary
# on exception, print error and exit program
try:
    words = open("D:\\school\\comp1352\\week2\\usaWords.txt")
except:
    print("usaWords.txt not found!")
    exit()

# create list of words
lines = words.readlines()

# remove line breaks from words in list
for i in range(len(lines)):
    if lines[i][-1:] == "\n":
        lines[i] = lines[i][0:-1]

wordleWords = []    # define list for five-letter words valid for Wordle targets

# add all five-letter words to list of Wordle targets
for item in lines:
    if len(item) == 5:
        wordleWords.append(item)

# function to determine if user's guess is valid Wordle guess
def isValid(userGuess:str) -> bool:
    """
        Determines if an user guess is a valid Wordle guess
        parameters: userGuess (input word)
        return: bool
    """

    # if guess isn't five letters, reject it
    # realistically this check isn't needed,
    # but i figure if we can rule out a guess without having to iterate over the entire Wordle list
    # it will save computing time
    if len(userGuess) != 5:
        return False
    
    # if the word is in the wordleWords list, a.k.a. if word is a valid english word, return true
    for item in wordleWords:
        if item == userGuess:
            return True
    
    # if all else fails, return false
    return False

# functions copied from assignment page for colored printing

# print with yellow background
def print_yellow(s, end='\n'):
   print('\u001b[43;1m', end='')
   print(s, end=end)
   print('\033[0m', end='')

# print with grey background
def print_grey(s, end='\n'):
   print('\u001b[47;1m', end='')
   print(s, end=end)
   print('\033[0m', end='')

# print with green background
def print_green(s, end='\n'):
   print('\u001b[42;1m', end='')
   print(s, end=end)
   print('\033[0m', end='')

# select random word from wordleWords list
target = wordleWords[random.randint(0, len(wordleWords))]
numGuesses = 0

# game loop
while True:
    guess = (input(f"Guess {numGuesses + 1}: "))

    if isValid(guess) == False:
        print(f"{guess} is NOT a valid guess. Please input a 5-letter english word.")
    else:
        numGuesses += 1
        output = ""

        # iterating over each character in the target
        for i in range(len(target)):
            # string to keep track of if the character is correct or not
            # i'm not sure doing it this way is required,
            # but without the substring method the game loop was
            # returning garbage, so this fixed the bug and i didn't look into it any further
            substring = ""

            # if character matches guess in the position, add "G" to substring
            if guess[i] == target[i]:
                substring += "G"
            else:
                # if character exists in guess, but not in the same position, add "Y" to substring
                for j in range(len(target)):
                    if guess[i] == target[j]:
                        substring += "Y"
            # if substring is blank, that means the character doesn't exist in target
            # so add "B" to substring
            if substring == "":
                substring += "B"
            # append substring to output
            output += substring

        # iterate over ouptut, using color print functions to print the guess with the Wordle colors
        # i think this can be done without using the output variable, saving memory,
        # but i already had output implemented before using the colored printing
        # so decided to reuse the variable to save time on implementing colored printing
        for i in range(len(output)):
            if output[i] == "B":
                print_grey(f" {guess[i]} ", end='')
            elif output[i] == "Y":
                print_yellow(f" {guess[i]} ", end='')
            else:
                print_green(f" {guess[i]} ", end='')
        
        # print a line break for visual clarity
        print("\n")

        # win condition: if all characters are green, that means the guess is correct
        if output == "GGGGG":
            print(f"The word was {target.upper()}. You got it in {numGuesses} guesses.")
            break

        # lose condition: if the number of guesses exceeds 6, the game is over
        if numGuesses >= 6:
            print(f"You lose. You failed to guess the word, {target.upper()}, in 6 guesses.")
            break
