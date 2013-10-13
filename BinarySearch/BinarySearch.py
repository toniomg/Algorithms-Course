'''
Created on 13 Oct 2013

@author: Antonio

Implementation of binary search
'''


def binarySearch(key, n):
    lo = 0
    hi = len(n)-1

    steps = 0
    
    while (lo <= hi):
        mid = int(lo + (hi - lo)/2)
        print (n[lo:hi])
        if key < n[mid] :
            hi = mid-1
            steps +=1
        elif key > n[mid]:
            lo = mid+1
            steps +=1
        else:
            return [mid, steps]
    
    
if __name__ == '__main__':
    print (binarySearch(5, range(100000000)))