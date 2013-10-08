class QuickFindUF:
    """ Implementation of the Quick-Find Algorithm"""
    id = []
    def __init__(self, n):
        for i in range(n):
            self.id.append(i)
            
    
    def connected(self, p, q):
        return self.id[p] == self.id[q]
    
    
    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if (self.id[i] == pid):
                self.id[i] = qid
                