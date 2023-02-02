"""
    An implementation of Pico Fermi Bagels in Python
    Filename: picofermibagels.py
    Author: XXXXX XXXXXX
    Date: 8jan22
    Course: COMP1352
    Assignment: Project 1
    Collaborators: None
    Internet Source: https://www.delftstack.com/howto/python/split-integer-into-digits-python/
"""

import random

def genTarget()->list:
    """
        Generates a three-digit target number for Pico Fermi Bagels, in list form
        parameters: None
        return: list
    """

    tg = []         # define list that we will eventually return

    # while loop that terminates once the list has grown 3 integers long
    while len(tg) < 3:
        randnum = random.randint(0, 9)

        # if list has no entries, append the number as it will be the first & therefore have no duplicates
        if len(tg) == 0:
            tg.append(randnum)
        # if the list does have entires, check for duplicates and only append the random number if it hasn't appeared yet in the list
        else:
            hasNum = False
            for num in tg:
                if (randnum == num):
                    hasNum = True
            if hasNum == False:
                tg.append(randnum)
    return tg       # return our constructed list

def isValid(gl:list)->bool:
    """
        Determines if an input number is a valid Pico Fermi Bagels guess
        parameters: gl (input number in list form)
        return: bool
    """

    # if the number is grater or less than three digits, reject it
    if not len(gl) == 3:
        return False

    # if the number has duplicate digits, reject it
    for i in gl:
        count = 0       # counter for how many times a digit has occured in the number
        for j in gl:
            if i == j:
                count += 1
        if count > 1:   # if digit has occured more than once, reject
            return False
    return True


target = genTarget()    # generate target for the game
numGuesses = 0          # initialize variable to hold number of guesses user has made

while True:
    guess = (input("Input a guess: "))

    # this try except block does two things in one go:
    # 1) checks if the user's inputted value is an integer (if it isn't, it can't be a valid guess)
    # 2) puts the guess into a list of numbers (to compare against target value)

    # this could have also been done with a string & probably save some memory,
    # but i ended up going with a list and it let me knock out both of these birds
    # with one code block, so maybe it's worth it. the world may never know
    try:
        guesslist = [int(i) for i in str(guess)]
    except:
        print("Please input a three-digit integer number")
        continue

    # if guess is valid, enter game loop
    if isValid(guesslist) == False:
        print("Invalid guess - guess must be a three-digit number with no duplicate digits")
    else:
        numGuesses += 1

        output = ""
        
        # iterating over each number in the target
        for i in range(len(target)):
            # if number matches guess in the position it's in, add "Fermi! " to output
            if guesslist[i] == target[i]:
                output += "Fermi! "
            else:
                for j in range(len(target)):
                    # if number exists in guess, but not in the same position, add "Pico! " to output
                    if guesslist[i] == target[j]:
                        output += "Pico! "
            
        # if we haven't added anything to output yet,
        # that means none of the guessed numbers are in the target.
        # so, we add "Bagels! " to the output
        if output == "":
            output += "Bagels! "
        
        print(output)

        # win condition: if output contains 3 "Fermi! "'s,
        # that means the user chose the correct number.
        # print number & amount of guesses
        if output == "Fermi! Fermi! Fermi! ":
            print(f"The number was {guess}. You got it in {numGuesses} guesses.")
            break
