class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return ""
        cur, s = self.head, str(self.head.data)
        while cur.next != None: 
            if self.size > 0:
                s += "->"
            s += str(cur.next.data)
            cur = cur.next
        return s

    def str_reverse(self):
        if self.isEmpty():
            return ""
        cur, s = self.tail, str(self.tail.data)
        while cur.previous != None:
            if self.size > 0:
                s += "->"
            s += str(cur.previous.data)
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self,data):
        p = Node(data)
        if self.head == None:
            self.head = p
            self.tail = p
            self.head.next = self.head.prev = None
        else:
            t = self.head
            while t != None:
                if t.next == None:
                    t.next = p
                    t.next.previous = t
                    break
                else:
                    t = t.next
            
            self.tail = p
        self.size += 1

    def addHead(self,data):
        p = Node(data)
        t = self.head
        self.head = p
        p.next = t
        t.previous = p
        t.previous = self.head
        self.size += 1

    def insert(self,index,data):
        p = Node(data)
        t = self.head
        count = 0
        if index == '0':
            if self.size == 0:
                self.head = self.tail = p
            else:
                self.head = p
                p.next = t
                t.previous = p
                t.previous = self.head
        else:
            while int(index) != count and count < self.size:
                count += 1
                t = t.next
                if count == int(index):
                    if count == self.size:
                        self.tail.next = p
                        p.previous = self.tail
                        self.tail = p
                    else:
                        p.previous = t.previous
                        t.previous.next = p
                        p.next = t
                        t.previous = p
                
        self.size += 1

    def remove(self,data):
        t = self.head
        count = 0
        if self.size > 0:
            if t.data == data:
                self.head = t.next
                t.next.previous = None
                self.size -= 1
                print('removed :',data,'from index :',count)
                return
            else:
                while t.next != None:
                    count += 1
                    if t.next.data == data:
                        t.next = t.next.next
                        t.next.previous = t
                        self.size -= 1
                        print('removed :',data,'from index',count)
                        return
                    else:
                        t = t.next
                print('Not Found!')
                return
        else:
            print('Not Found!')

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "A ": #append
        L.append(i[2:])
    elif i[:2] == "Ab": #add before
        L.addHead(i[3:])
    elif i[:1] == "I": #insert
        data = i[2:].split(':')
        if int(data[0]) >= 0 and int(data[0]) <= L.size:
            print('index =',data[0],'and data =',data[1])
            L.insert(data[0],data[1]) #insert(index,data)
        else:
            print('Data cannot be added')
    elif i[:1] == "R": #remove
        L.remove(i[2:])
    print('linked list :',L)
    print('reverse :',L.str_reverse())
#input = A 3,A 4,Ab 0,I 1:2