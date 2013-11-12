'''
Created on 12 Nov 2013

@author: toniomg
'''

class bNode():
    
    leftNode = None
    rightNode = None
    data = 0
    
    def __init__(self, rightNode, leftNode, data):
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.data = data
    
        
    
class BinaryTree():
    '''
    Simple binary tree
    '''

    rootNode = None

    def __init__(self):
        '''
        Constructor
        '''
        
    def insertData(self, root, data):

        if root == None:
            #insert node at the root
            return bNode(None, None, data)
        else:
            if data <= root.data: 
                root.leftNode = self.insertData(root.leftNode, data)
            else:
                root.rightNode = self.insertData(root.rightNode, data)
        return root
    
    def traverseTree(self, root):
        print(root.data)
        if root.leftNode != None:
            self.traverseTree(root.leftNode)
        if root.rightNode != None:
            self.traverseTree(root.rightNode)
        return
        
        
    
    

if __name__ == "__main__":
    tree = BinaryTree()
    root = bNode(None, None, 10)
    tree.rootNode = root;
    tree.insertData(root, 5)
    tree.insertData(root, 6)
    tree.insertData(root, 3)
    tree.insertData(root, 12)
    tree.traverseTree(root)
    
                
            
            
            
            
    
            
            
            
        
        