'''
 * กลุ่มที่  : 20010102
 * 62010436 ธีรดนย์ จันทร์หอม
 * chapter : 6	item : 1	ครั้งที่ : 0001
 * Assigned : Friday 11th of September 2020 10:47:14 AM --> Submission : Friday 11th of September 2020 12:01:54 PM	
 * Elapsed time : 74 minutes.
 * filename : lab41.py
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.Size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p = Node(item)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
        self.Size += 1

    def addHead(self, item):
        t = self.head
        p = Node(item)
        self.head = p
        p.next = t
        self.Size += 1

    def search(self, item):
        t = self.head
        while t != None:
            if t.value == item:
                return 'Found'
            else:
                t = t.next
        return 'Not Found'

    def index(self, item):
        t = self.head
        indexNum = 0
        while t != None:
            if t.value == item:
                return indexNum
            else:
                t = t.next
                indexNum += 1
        return -1

    def size(self):
        return self.Size

    def pop(self, pos):
        t = self.head
        while t != None:
            if pos == 0:
                self.head = t.next
                self.Size -= 1
                return 'Success'
            v = t.next.value
            if self.index(v) == pos:
                self.Size -= 1
                if t.next == None:
                    t = None
                else:
                    t.next = t.next.next
                return 'Success'
            else:
                t = t.next
        return 'Out of Range'

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1}".format(L.search(i[3:]), i[3:]),'in',L)
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
# inp = input('Enter txt:')
# L.append(L)
# inp = iinp)
# print(nput('Enter another txt:')
# L.append(inp)
# print(L)