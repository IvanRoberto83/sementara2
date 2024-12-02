from node import Node

class BinaryTree:
    def __init__(self):
        self._root = None
        self._size = 0
    
    def add(self,data):
        if self._root is None:
            self._root = Node(data, None)
            self._size += 1
        else:
            if self._root.insert(data):
                self._size += 1
                
    def size(self):
        return self._size
    
    def empty(self):
        return self._size == 0
    
    def nodes(self):
        return self.inorder(self._root)
    
    def printNodes(self):
        self.inorder(self._root)
    
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left())
            print(node.operator(), end=" ")
            self.inorder(node.right())

    def search(self,value):
        return self.binarySearch(self._root, value) is not None
    
    def binarySearch(self, node, value):
        if node is None or node.operator() == value:
            return node
        elif value < node.operator():
            return self.binarySearch(node.left(), value)
        else:
            return self.binarySearch(node.right(), value)
        
    def expandExternal(self,value):
        node = self.binarySearch(self._root, value)
        if node is not None and node.isExternal():
            node.insert(node.operator()-1)
            node.insert(node.operator()+1)
            self._size += 2
    
    def removeAboveExternal(self,value):
        node = self.binarySearch(self._root,value)
        if node is not None:
            sibling = node.parent().left() if node.parent().right() else node.parent()
            if node.parent() == self._root:
                self._root = sibling
                sibling.setParent(None)
            else:
                if node.parent() == node.parent().parent().left():
                    node.parent().parent().setLeft(sibling)
                else:
                    node.parent().parent().setRight(sibling)
            
        self._size+=2    

bt = BinaryTree()
bt.add(10)
bt.add(5)
bt.add(7)
bt.add(1)
bt.add(15)
bt.add(9)
bt.add(25)
bt.add(90)
bt.printNodes()
print()
print(bt.search(10))
print("================================")
bt.expandExternal(9)
bt.printNodes()
print()
bt.removeAboveExternal(7)
bt.printNodes()