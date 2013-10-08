from QuickUnionUF import QuickUnionUF
from QuickFindUF import QuickFindUF
import unittest


class TestUnionFind(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def testUnionFind(self):
        self.uf = QuickUnionUF(10)
        self.assertFalse(self.uf.connected(0, 1), "")
        self.uf.union(0, 6)
        self.uf.union(8,9)
        self.uf.union(6,8)
        self.uf.union(1,7)
        self.assertFalse(self.uf.connected(0, 1), "")
        self.uf.union(7,9)
        self.assertTrue(self.uf.connected(0,1), "")
        
    def testQuickFind(self):
        self.uf = QuickFindUF(10)
        self.uf.union(0, 6)
        self.uf.union(8,9)
        self.uf.union(6,8)
        self.uf.union(1,7)
        self.assertFalse(self.uf.connected(0, 1), "")
        self.uf.union(7,9)
        self.assertTrue(self.uf.connected(0,1), "")

        
        
        
        
if __name__ == '__main__':
    unittest.main()