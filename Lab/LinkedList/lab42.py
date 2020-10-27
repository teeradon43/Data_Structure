"""
Chapter : 6 - item : 2 - Doubly Linked List(append,insert,remove)
ให้เขียนคลาสของ Doubly Linked List ซึ่งมีเมท็อดดังนี้

1. def __init__(self): สำหรับสร้าง linked list
2. def __str__(self): return string แสดง ค่าใน linked list
3. def str_reverse(self): return string แสดง ค่าใน linked list จากหลังมาหน้า
4. def isEmpty(self): return list นั้นว่างหรือไม่
5. def append(self, data): add node ที่มี data เป็น parameter ข้างท้าย linked list
6. def insert(self, index, data): insert data ใน index ที่กำหนด
7. def remove(self, data): remove & return node ที่มี data

 - การแทรกในที่นี้ จะเป็นการนำข้อมูลใหม่ที่ต้องการมาใส่แทนที่ตำแหน่งของข้อมูลเดิมและย้ายข้อมูลเดิมไปต่อหลังข้อมูลใหม่ 

คำแนะนำเพิ่มเติม เพื่อความง่ายในการเขียนโค้ดและไม่ต้องเขียนspecial caseเยอะๆ ให้ลองใช้ Dummy Node ดูนะครับ
(หากสงสัยการใช้งาน Dummy Node สอบถามพี่ๆTA หรือ https://youtu.be/XgUIjTQ1HjA )

โดยรูปแบบ Input มีดังนี้
1. append       ->  A
2. add_before -> Ab
3. insert          ->   I
4. remove       ->  R

*******ให้ใช้ class Node ในการทำ Linked List ห้ามใช้ list*********
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
"""

"""
TEST CASE
Testcase student: #1/6
Enter Input : A 3,A 4,Ab 0,I 1:2
linked list : 3
reverse : 3
linked list : 3->4
reverse : 4->3
linked list : 0->3->4
reverse : 4->3->0
index = 1 and data = 2
linked list : 0->2->3->4
reverse : 4->3->2->0

Testcase student: #2/6
Enter Input : I -1:0,I 10:10,I 0:0
Data cannot be added
linked list : 
reverse : 
Data cannot be added
linked list : 
reverse : 
index = 0 and data = 0
linked list : 0
reverse : 0

Testcase student: #3/6
Enter Input : R 0,A 1,A 1,A 2,R 1
Not Found!
linked list : 
reverse : 
linked list : 1
reverse : 1
linked list : 1->1
reverse : 1->1
linked list : 1->1->2
reverse : 2->1->1
removed : 1 from index : 0
linked list : 1->2
reverse : 2->1

Testcase student: #6/6
Enter Input : I 1:1,I 0:0,I 0:1,I 0:2,I 3:-1,I -1:-1,I 10:5,I 2:0
Data cannot be added
linked list : 
reverse : 
index = 0 and data = 0
linked list : 0
reverse : 0
index = 0 and data = 1
linked list : 1->0
reverse : 0->1
index = 0 and data = 2
linked list : 2->1->0
reverse : 0->1->2
index = 3 and data = -1
linked list : 2->1->0->-1
reverse : -1->0->1->2
Data cannot be added
linked list : 2->1->0->-1
reverse : -1->0->1->2
Data cannot be added
linked list : 2->1->0->-1
reverse : -1->0->1->2
index = 2 and data = 0
linked list : 2->1->0->0->-1
reverse : -1->0->0->1->2


"""
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
