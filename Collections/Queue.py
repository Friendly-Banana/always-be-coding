class Queue:
    """
    basic Queue
    uses a List under the hood"""

    def __init__(self, items=()):
        self.items = list(items)

    def __str__(self):
        return "Queue {" + ", ".join(str(i) for i in self.items) + "}"

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        # list is not empty
        if self.items:
            return self.items.pop(len(self.items) - 1)

    def isEmpty(self):
        return len(self.items) == 0
