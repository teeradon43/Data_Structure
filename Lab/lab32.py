"""
Chapter : 4 - item : 2 - PSD48 a.k.a เขาเรียกผมว่าเอเรน
PSD48 (P-Saderd 48 Group) เป็นวงไอดอลวงหนึ่งที่กระแสกำลังมาแรง ณ ตอนนี้โดยเพลงที่ได้รับความนิยมอย่างมากคือเพลงจี่หอย
โดยวง PSD48 กำลังจะจัดงานจับมือขึ้น โดยมีกฎอยู่ว่าถ้าหากคนที่กำลังต่อแถวอยู่เป็นคนจาก กองกำลังสำรวจ 
จะได้สิทธิพิเศษในการแทรกแถวไปข้างหน้าสุดทันที (แต่ถ้าหากคนหน้าสุดก็เป็นคนของกองกำลังสำรวจก็ต้องต่อหลังเขาอยู่ดี)  
PSD48 อยากให้คุณช่วยเขียนโปรแกรมสำหรับหาว่าจะมีโอตะ id ใดบ้างที่ได้จับมือ

เพลงประกอบ : https://youtu.be/Jd4Hd-HFgls

Input :
EN <value>  เป็นโอตะธรรมดา  id = value
ES <value>  เป็นโอตะของกองกำลังสำรวจ  id = value
D                  เป็นคำสั่งแสดงผล value ของหัวแถว ถ้าหากในแถวไม่มีคนจะแสดงคำว่า Empty
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

sQ = Queue()
nQ = Queue()
txt = input('Enter Input : ').split(',')
for i in txt:
    j = i.split(' ')
    if j[0] == 'EN':
        nQ.enqueue(j[1])
    elif j[0] == 'ES':
        sQ.enqueue(j[1])
        pass #เก็บ value ไว้ว่าเป็น ES แล้วเอาไปต่อ ES ข้างหน้า
    else:
        if nQ.size() > 0 or sQ.size() > 0:
            if sQ.size() > 0:
                print(sQ.dequeue())
            else:
                print(nQ.dequeue())
        else:
            print('Empty')