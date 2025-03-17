class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        return self.items

    def size(self):
        return len(self.items)
