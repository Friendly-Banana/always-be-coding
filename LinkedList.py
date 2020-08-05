class LinkedList():
    def __init__(self):
        self.head = None
    
    def __repr__(self):
       return f"Instance of LinkedList  head exists: {bool(self.head)} len: {len(self)}"
       
    def __str__(self):
        return "Instance of LinkedList"
        
    def __len__(self):
        i = 0
        p = self.head
        while p != None:
            i += 1
            p = p.next
        return i
         
    def __delitem__(self, key):
        temp = self[key + 1]
        if key == 0:
            deleted = self.head
            del self.head
            self.head = temp
        else:
            deleted = self[key]
            del self[key]
            self[key - 1].next = temp
        return deleted
            
    def __getitem__(self, key):
        i = 0
        p = self.head
        while i < key:
            if p == None:
                raise IndexError("Index out of bounds")
            i += 1
            p = p.next
        return p
        
    def __setitem__(self, key, value):
            self[key].item = value
    
    def append(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp 
            return
        node = self.head
        while node.next != None:
            node = node.next
        node.next = temp
     
    def isEmpty():
        return self.head == None

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
