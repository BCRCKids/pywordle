import random
from termcolor import colored

def print_green (text):
    print_text = colored (text, "white", "on_green")
    print (print_text, end="")
def print_red (text):
    print_text = colored (text, "white", "on_red")
    print (print_text, end="")
def print_yellow (text):
    print_text = colored (text, "white", "on_yellow")
    print (print_text, end="")
guesses = 5
lines = []
#Read the words from the words file
with open("sgb-words.txt", "r") as f:
    lines = [line.rstrip("\n") for line in f]
#choose a random word from the list of words
random_word = random.choice (lines)

while True:
    #Get the user's word
    givenWord = input ("Enter a five letter word: ")

    ##verify user input
    while (True):
        if len(givenWord) != 5:
            #If it's not a five letter word
            givenWord = input ("A FIVE letter word, man...\n")
        elif (givenWord not in lines):
            #If it's not in the words list
            givenWord = input ("An actual WORD man...\n")
        else:
            break

    #Print out the guess result
    for i in range (len(random_word)):
        if random_word[i] == givenWord[i]:
            print_green (givenWord[i])
        elif givenWord[i] in random_word :
            print_yellow (givenWord[i])
        else :
            print_red(givenWord[i])
    print ("")
    
    guesses -= 1

    if givenWord == random_word :
        print ("You guessed it!")
        break
    elif guesses == 0:
        print ("Out of guesses! The word was: " + random_word)
        break
    else:
        print ("Not Quite! Guesses remaining: " + str(guesses))
