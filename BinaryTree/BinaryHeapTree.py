'''
Created on 12 Nov 2013

@author: toniomg
'''

class bNode():
    
    leftNode = None
    rightNode = None
    parentNode = None
    data = 0
    
    def __init__(self, parentNode, data):
        self.parentNode = parentNode
        self.data = data
    
        
    
class BinaryHeapTree():
    '''
    Simple binary tree
    '''

    rootNode = None

    def __init__(self):
        '''
        Constructor
        '''
    
    def insertData(self, root, data):
        self.insertHeapData(None, root, data)

        
    def insertHeapData(self, parentNode, root, data):

        if root == None:
            #insert node at the root
            node = bNode(parentNode, data)
            #self.swapParent(node)
            return node
        else:
            if data <= root.data: 
                root.leftNode = self.insertHeapData(root, root.leftNode, data)
            else:
                root.rightNode = self.insertHeapData(root, root.rightNode, data)
        return root
    
    def maxK(self, root):
        if root.rightNode == None:
            return root.data
        else:
            return self.maxK(root.rightNode)
    
    def minK(self, root):
        if root.leftNode == None:
            return root.data
        else:
            return self.minK(root.leftNode)
        
    def swapParent(self, root):
        if root.parentNode != None:
            if root.parentNode.data < root.data:
                root.parentNode.data, root.data = root.data, root.parentNode.data
                self.swapParent(root.parentNode)
    
    
    def traverseTree(self, root):
        print(root.data)
        if root.leftNode != None:
            self.traverseTree(root.leftNode)
        if root.rightNode != None:
            self.traverseTree(root.rightNode)
        return
        
        
    
    

if __name__ == "__main__":
    tree = BinaryHeapTree()
    root = bNode(None, 0)
    tree.rootNode = root;
    tree.insertData(root, 1)
    tree.insertData(root, 2)
    tree.insertData(root, 3)
    tree.insertData(root, 4)
    tree.insertData(root, 5)
    tree.insertData(root, 6)
    tree.traverseTree(root)
    print(tree.maxK(root))
    print(tree.minK(root))
    
                
            
            
            
            
    
            
            
            
        
        