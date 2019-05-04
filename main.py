'''
Created on 30 Mar 2019

@author: Chester
'''

import random
import numpy as np
from threading import currentThread

numberOfThrows=10
boardSize=10 
#for now do 1D case as the dimensions don't meaningfully interact

Guess= np.zeros(numberOfThrows+1)
Guess[0]=boardSize/2.0

Throws=np.zeros(numberOfThrows+1)

Throws[0]=random.uniform(0,boardSize) #first 'Throw' is the target
exactMatchCounter=0

def findSign(landPos, actualPos):
    '''
    Finds direction of throw relative to actual position.
    Probably a more mathsy way to do this than with logic
    '''
    
    if (landPos<actualPos):
        return +1
    elif (landPos>actualPos):
        return -1
    else:
        exactMatchCounter+=1
        return 0
    
def throw(size):
    '''
    This is a function in case I wanted to implement more logic in this
    '''
    
    return random.uniform(0,size)

def guessDiff(guess,pos):
    '''
    Calculates difference between actual position and guesses
    '''
    
    diff=np.zeros(numberOfThrows)
    
    for i in range(1,numberOfThrows+1):
        diff[i-1]=pos-guess[i]
               
    return diff


def guessLogic(noOfThrows,currentThrow,Guesses,actualPosition):
    '''
    Basic +- to guess doesn't work, trying an averaging approach
    This is hopefully similar to how  a human would process this information
    
    This is probably no different to just taking all the +-s and averaging them
    but this makes more 'logical' sense
    '''
    avg=0
    
    for j in range(0,noOfThrows):
        avg+=Guesses[j]
    
    avg/=noOfThrows*1.0
    
    return avg+findSign(currentThrow, actualPosition)



for i in range(1,numberOfThrows+1):
    Throws[i]=throw(boardSize)
        
    Guess[i]= guessLogic(i,Throws[i],Guess,Throws[0])
    
#print(Position,Guess[-1])
print(guessDiff(Guess, Throws[0]))
#print(Throws)