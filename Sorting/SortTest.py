'''
Created on 20 Oct 2013

@author: Antonio
'''
import unittest
from SelectionSort import selectionSort
from InsertionSort import insertionSort

class Test(unittest.TestCase):


    def testSort(self):
        testSorted = [1, 3, 5, 6]
        
        test1 = [1 ,3, 5, 6]
        self.assertEqual(selectionSort(test1), testSorted, 0)
        self.assertEqual(insertionSort(test1), testSorted, 0)
        
        test2 = [1, 3, 6, 5]
        self.assertEqual(selectionSort(test2), testSorted, 0)
        self.assertEqual(insertionSort(test2), testSorted, 0)
        
        test3 = [6, 5, 3, 1]
        self.assertEqual(selectionSort(test3), testSorted, 0)
        self.assertEqual(insertionSort(test3), testSorted, 0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSelectionSort']
    unittest.main()