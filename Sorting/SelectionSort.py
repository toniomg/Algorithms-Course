'''
Created on 20 Oct 2013

@author: Antonio
'''

def selectionSort(n):
    """ Sort the array of integers using Selection Sort"""
    
    for i in range(len(n)):
        #Look for the smallest
        smallest = i;
        for j in range(i+1,len(n)):
            if n[j] < n[smallest]:
                smallest = j
        #Swap them
        n[i], n[smallest] = n[smallest], n[i]
        print(n)
    
    return n
        