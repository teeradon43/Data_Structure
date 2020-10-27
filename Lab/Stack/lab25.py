"""
Chapter : 5 - item : 5 - วันหนึ่งฉันเดินเข้าป่า (2) a.k.a Into the Woods but หลอนประสาท
หลังจากกฤษฎาเดินหลงป่ามาได้สักพักก็ได้ไปเจอเห็ดสีสันสวยงามจึงได้หยิบขึ้นมากิน  หลังจากกินเข้าไปทำให้กฤษฎามีอาการแปลกๆเกิดขึ้น  
เนื่องจากเห็ดที่กินเข้าไปเป็นเห็ดพิษ  แต่กฤษฎาก็ยังคอยนับความสูงต้นไม้ไปเรื่อยๆเหมือนเดิม  ผลข้างเคียงจากเห็ดพิษก็ได้ส่งผลกระทบต่อการนับต้นไม้
ของกฤษฎาเนื่องจากอาการหลอนประสาท ทำให้ต้นไม้ที่มีความสูงเป็นเลขคี่มีการเพิ่มความสูงมา 2 เมตร และต้นไม้เลขคู่ลดความสูงไป  1 เมตร 
ความสูงที่น้อยที่สุดคือ 1 เมตร

ให้น้องๆเขียนโปรแกรมเพื่อรับความสูงของต้นไม้ที่กฤาฎาได้เดินผ่าน  แล้วหาว่าเมื่อกฤษฎาหันหลังกลับมามองจะเห็นต้นไม้กี่ต้น

อธิบาย Input :  A  <Heights>  แสดงถึงความสูงของต้นไม้  ,  B  คือการหันหลังกลับมามอง , S  คือการโดนผลกระทบจากเห็ดพิษ

อธิบาย Test Case แรก : กฤษฎาจะเดินผ่านต้นไม้ความสูง  4   ก่อนแล้วตามด้วย  3   แล้วหันหลังกลับมามองจะเห็นต้นไม้ 2 ต้น 
ต่อมาเดินไปเจอต้นไม้สูง  5  กับ ต้นไม้สูง 8 ตามลำดับ  แล้วหันหลังกลับมามองจะเห็นแค่ต้นไม้ต้นเดียว  
เนื่องจากต้น 8 เมตรบังต้นไม้ความสูง  4  3  และ  5 

โดยจะรับประกันว่าจะมีต้นไม้อย่างน้อย 1 ต้นและมีการหันกลับมาอย่างน้อย 1 ครั้ง
"""

class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == [] or len(self.items) == 0

    def size(self):
        return len(self.items)

s = Stack()
s2 = Stack()
txt = input('Enter Input : ').split(',')
for i in txt:
    chr = i.split()
    if chr[0] == 'A':
        # while not s.isEmpty():
        #     if int(s.peek()) <= int(chr[-1]):
        #         s.pop()
        #     else:
        #         break
        s.push(chr[-1])
    elif chr[0] == 'S':
        while not s.isEmpty():
            if int(s.peek()) % 2 == 1:
                s2.push(int(s.pop())+2)
            else:
                s2.push(int(s.pop())-1)
        while not s2.isEmpty():
            while not s.isEmpty():
                if int(s.peek()) <= int(s2.peek()):
                    s.pop()
                else:
                    break
            s.push(s2.pop())
    else:
        count = 0
        while not s.isEmpty():
            if not s2.isEmpty():
                if int(s.peek()) >= int(s2.peek()):
                    count += 1
                    s2.push(s.pop())
                else:
                    break
            else:
                s2.push(s.pop())
                count += 1
        while not s2.isEmpty():
            s.push(s2.pop())

        print(count)