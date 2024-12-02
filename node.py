class Node:
    def __init__(self, data, parent):
        self._data = data
        self._parent = parent
        self._left = None
        self._right = None
        
    def insert(self, data):
        if data < self.operator():
            if self._left is None:
                self._left = Node(data, self)
            else:
                self._left.insert(data)

        elif data > self.operator():
            if self._right is None:
                self._right = Node(data, self)
            else:
                self._right.insert(data)
                
        else:
            return False
        return True
    
    def operator(self):
        return self._data
        
    def left(self):
        return self._left
    
    def right(self):
        return self._right
    
    def parent(self):
        return self._parent
    
    def isRoot(self):
        return self._parent is None
    
    def isExternal(self):
        return self._left is None and self._right is None