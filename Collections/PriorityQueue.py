"""
PriorityQueue
Uses a dictionary with the priority as key and a list with the values
"""
class PriorityQueue():
    def __init__(self):
        self.items = dict()
        
    def is_empty(self):
        return len(self.items) == 0
    
    def insert(self, value, key):
        # check if key already exists 
        if key in self.items.keys():
            self.items[key].append(value)
        else:
            self.items[key] = [value]
        
    def pop(self):
        key = max(self.items.keys())
        # check if we have multiple values
        if len(self.items[key]) > 1:
            value = self.items[key].pop(0)
        else:
            value = self.items[key][0]
            # delete unused key
            del self.items[key]
        return value
        
    def peek(self):
        return self.items[max(self.items.keys())]