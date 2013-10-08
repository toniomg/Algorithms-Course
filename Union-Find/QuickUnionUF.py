class QuickUnionUF:
    """ Implementation of the Quick-Union Algorithm"""
    id = []
    def __init__(self, n):
        for i in range(n):
            self.id.append(i)
            
    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i
            
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        i =self.root(p)
        j = self.root(q)
        self.id[i] = int(j)
        
        
