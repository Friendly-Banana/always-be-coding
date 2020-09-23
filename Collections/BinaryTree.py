class BinaryTree():
    def __init__(self, *values):
        values = sorted(*values)
        # even amount of values
        self.has_value = len(values) % 2 == 1     
        #self.value = 3
        
    def append(self, value):
        pass
    
class BinaryNode():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

BinaryTree ([2, 3, 5, 1, 6, 2])