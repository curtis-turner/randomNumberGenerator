#Author: Curtis Turner
#Email: cjturner@csu.fullerton.edu
#Description: This file contains the main python program for executing a guessing game using Lemher's Algorithm

import sys
import getopt
import time

from MyPRNG import PRNG



def hotorcold(random,gList, gCount):
    if gCount == 0:
        print("Nice first guess try guessing again.")
        return
    delta = abs(random-gList[gCount])
    deltaTwo = abs(random - gList[gCount - 1])
    if delta > deltaTwo:
        print("OOPS!, You're getting COLDER")
    elif deltaTwo > delta:
        print("You're getting WARMER.")
 
def getNewRandom(oldRandom, n, m):
    return PRNG.next_prn(oldRandom, n, m)

def usage():
    helpText = open('usage.txt', 'r')
    print(helpText.read())


def main():
    guessList = []
    guessCount = 0
    sd = 0
    minimum = 0
    maximum = 0
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h:v:s:n:x', ['help', 'verbose', 'seed=', 'min=', 'max='])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
        verbose = False
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit(2)
        elif opt in ('-v', '--verbose'):
            verbose = True
        elif opt in ('-s', '--seed'):
            sd = arg
        elif opt in ('-n', '--min'):
            minimum = arg
        elif opt in ('-x', '--max'):
            maximum = arg
        else:
            usage()
            sys.exit(2)
            
    if sd == 0:
        sd = time.clock()
    if minimum == 0:
        minimum = 1
    if maximum == 0:
        maximum =1000
    sd = int(sd)
    minimum = int(minimum)
    maximum = int(maximum)
    
    #print(sd)
    #print(minimum)
    #print(maximum)
    
    newPRNG = PRNG()
    newPRNG.seed(sd)
    firstRandom = newPRNG.newRandom(minimum, maximum)
    #print(firstRandom)
    while True:
        #print(firstRandom)
        guess = int(input("Please enter your guess >> "))
        if guess == 0:
            print("Thanks for playing guess a number!")
            break
        elif guess == firstRandom:
            print("Hurray you guessed the right number good job!!!")
            print("Generating new Random Number prepare your next guess.")
            print("Or enter 0 to quit.")
            firstRandom = getNewRandom(firstRandom, minimum, maximum)
            guessList = []
            guessCount = 0
        else:
            #print(PRNG)
            guessList.append(guess)
            #print(guessList[0])
            #print(len(guessList))
            #print(guessCount)
            hotorcold(firstRandom, guessList, guessCount)
            print("Sorry that's not right :(. Guess again or enter 0 to end the game.")
            guessCount+=1
        

        print(guessCount)
        #print(getNewRandom(firstRand, minimum, maximum))

    
if __name__ == "__main__":
    main()
