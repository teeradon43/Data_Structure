"""
Chapter : 4 - item : 1 - Basic Queue
เขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา

E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผลค่าที่ทำการ enqueue และ index ของตัวที่ทำการเพิ่มเข้าไป
D  ให้ทำการ dequeue ตัวที่อยู่หน้าสุดของ Queue ออกและแสดงตัวเลขที่เอาออกและแสดงขนาดของ Queueหลังจากทำการ dequeue แล้ว

*** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty ***
"""

class Queue:
    def __init__(self):
        self.item = []

    def enqueue(self,item):
        self.item.append(item)

    def dequeue(self):
        if self.size() > 0:
            return self.item.pop(0)

    def size(self):
        return len(self.item)

s = Queue()
txt = input('Enter Input : ').split(',')
for i in txt:
    j = i.split(' ')
    if j[0] == 'E':
        print('Add',j[1],'index is',s.size())
        s.enqueue(j[1])
    else:
        if s.size() > 0:
            print('Pop',s.dequeue(),'size in queue is',s.size())
        else:
            print('-1')

if s.size() > 0:
    print("Number in Queue is : ",s.item)
else:
    print('Empty')