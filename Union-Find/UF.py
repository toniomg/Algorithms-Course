class UF:
    """Represents a Union - Find structure"""
    union = []
    def __init__(self, n):
        self.n = n
        
    def addUnion(self, p, q):
        self.union.append([p, q])
    
    def connected(self, p, q):
        pass
    
    
#Open the file

f = open('nodes', 'r')
n = f.readline()

uf = UF(n)

#Read the unions
for line in f:
    pq = line.split()
    uf.addUnion(pq[0], pq[1])
    