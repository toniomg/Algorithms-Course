'''
Created on 20 Oct 2013

@author: Antonio
'''

def insertionSort(n):
    """Sort the integer using insertion sort
    """
    
    for i in range(len(n)):
        item  = n[i]
        for j in reversed(range(0, i)):
            if n[j] <= item:
                break  
            else:
                n[i],n[j] = n[j], n[i]
        print (n)
    
    return n