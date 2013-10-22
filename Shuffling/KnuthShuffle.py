'''
Created on 22 Oct 2013

@author: Antonio

Implementation of the Knuth Shuffle Algorithm
'''
import random

if __name__ == '__main__':
    initialList = [1, 2, 3, 4, 'a', 'b', 'c']
    print (initialList)
    
    for i in range(1,len(initialList)):
        r = random.randrange(i)
        initialList[i], initialList[r] = initialList[r], initialList[i] 
        
    print (initialList)
        