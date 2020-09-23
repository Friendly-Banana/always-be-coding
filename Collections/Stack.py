class Stack:
    def __init__(self):
        self.items = list()
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop(len(self.items))
        
    def top(self):
        return self.items[len(self.items)]