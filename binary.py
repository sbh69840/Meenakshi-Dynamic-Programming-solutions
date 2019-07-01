class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    def printTree(self):
        
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
def addTree(root):
        if not root:
            return
        
        addTree(root.left)
        addTree(root.right)
        final = root.data
        if root.left:
            final+=root.left.data
        if root.right:
            final+=root.right.data
        root.data = final
        
        
root = Node(12)
root.insert(19)
root.insert(8)
root.insert(7)
root.insert(6)
root.insert(5)
root.insert(4)
root.insert(3)
root.insert(2)
root.insert(1)
root.printTree()
addTree(root)
root.printTree()
    
