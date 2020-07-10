
class Queue:
    def __init__(self):
        # front of list is first element added
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self):
        self.items = self.items[1:]

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return self.items == []

