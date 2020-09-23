"""
basic Queue
uses a List under the hood
"""
class Queue():
    def __init__(self,  *args):
        self.items = list()
        for item in args:
            self.enqueue(item)
        
    def __str__(self):
        return "Queue [" + ", ".join([str(i) for i in self.items]) + "]"
        
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        # list is not empty
        if self.items:
            return self.items.pop(len(self.items) - 1)