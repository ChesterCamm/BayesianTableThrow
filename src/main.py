'''
Created on 30 Mar 2019

@author: Chester
'''

import random
import numpy as np

numberOfThrows=10
boardSize=10 
#for now do 1D case as the dimensions don't meaningfully interact

Guess= np.zeros(numberOfThrows+1)
Guess[0]=boardSize/2.0

Throws=np.zeros(numberOfThrows)

Position=random.uniform(0,boardSize)
exactMatchCounter=0

def findSign(landPos, actualPos):
    
    if (landPos<actualPos):
        return +1
    elif (landPos>actualPos):
        return -1
    else:
        exactMatchCounter+=1
        return 0
    
def throw(size):
    return random.uniform(0,size)

def guessDiff(guess,pos):
    diff=np.zeros(numberOfThrows)
    
    for i in range(1,numberOfThrows+1):
        diff[i-1]=pos-guess[i]
               
    return diff



for i in range(1,numberOfThrows+1):
    Throws[i-1]=throw(boardSize)
    
    Guess[i]=Guess[i-1]+findSign(Throws[i-1], Position)
    
print(guessDiff(Guess, Position),Position)