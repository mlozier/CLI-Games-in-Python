import time
import random


def printTrack():
    spacer = 10
    printRight = False
    
    randDirection = random.randrange(7,10)

    while True:
        # .2 seems to be the ideal challenge
        time.sleep(.4)
        
        if printRight == True:
            spacer += 1
        else:
            spacer -= 1

        print(" " * spacer + "X" + "     " + "X")
        
        if spacer < randDirection:
            printRight = True
            randDirection = random.randrange(4,15)
        if spacer > randDirection:
            printRight = False
            randDirection = random.randrange(4,15)

printTrack()