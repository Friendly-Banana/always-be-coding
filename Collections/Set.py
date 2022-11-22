class Set:
    def __init__(self, *items):
        self.items = list()
        for item in items:
            if item not in self.items:
                self.items.append(item)

    def __str__(self):
        return "Set {" + ", ".join([str(i) for i in self.items]) + "}"

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        self.items[key] = value

    def __delitem__(self, key):
        del self.items[key]
