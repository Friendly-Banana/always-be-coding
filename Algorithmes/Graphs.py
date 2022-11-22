class Node:
    def __init__(self, value, childs=list(), parent=None):
        self.value = value
        self.childs = childs
        self.parent = parent

    def set_parent(self, new_parent):
        if self.parent:
            self.parent.childs.remove(self)
        self.parent = new_parent
        self.parent.childs.append(self)

    def add_childs(self, new_children):
        for node in new_children:
            node.set_parent(self)


def draw(root):
    print(root.value)
    for child in root.childs:
        draw(child)


head = Node(1)
n1 = Node(2)
head.childs.append(n1)  # .set_parent(head)
draw(head)
