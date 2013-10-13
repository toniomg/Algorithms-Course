'''
Created on 13 Oct 2013

@author: Antonio
'''

#Implementation of the 3SUM algorithm using brute force


def find3SUM(n):
    
    count = 0
    for i in n[:len(n)]:
        for j in n[1:len(n)]:
            for k in n[2:len(n)]:
                if i + j + k == 0:
                    count+=1
                    
    return count
        
    
