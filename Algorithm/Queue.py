class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def isEmpty(self):
        return len(self.items) == 0 or self.items == []

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        if self.isEmpty():
            print('List is empty.')
        else:
            self.items.pop(0)

    def size(self):
        return len(self.items)

    def isFull(self): # if queue has limited size
        pass
    