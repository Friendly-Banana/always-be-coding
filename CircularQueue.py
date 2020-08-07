class CircularQueue():
    def __init__(self, length):
        self.length = length
        self.items = list()
        self.reader = 0
        self.writer = 0
        
    def read(self):
        value = self.items[self.reader]
        self.reader = (self.reader + 1) % self.length
        return value
    
    def write(self, *values):
        for value in values:
            nextIndex = (self.writer + 1) % self.length
            if self.writer != nextIndex:
                self.items[self.writer] = value
                self.writer = nextIndex
