class lists:

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def append(self, data):
        if self.head is None:
            p = node(data)
            p.next = None
        else:
            p = node(self.head)
            while p.next is not None:
                p = p.next
            p.next = data
            p.next = None

    # def size(self):
    #     p = node(self.head)


    def __str__(self):
        s = 'Linked Data : '
        p = self.head
        

class node:

    def __init__(self, data, next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next

    def __str__(self):
        node = self
        while node != None:
            print(node.data)
            node = node.next