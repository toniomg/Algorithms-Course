'''
Created on 13 Oct 2013

@author: Antonio
'''
import unittest
from ThreeSUMBruteForce import find3SUM 


class Test(unittest.TestCase):


    def testName(self):
        #1 2 3 -4 -10 -3 -5 -2 7 3 -1 0
        n = [1, 2, 3, -4, -10, -3, -5, -2, 7, 3, -1, 0]
        foundValue = 71
        foundAlg = find3SUM(n)
        self.assertEqual(foundAlg, foundValue, 'Algorithm has failed')
        
        pass


if __name__ == "__main__":
    unittest.main()