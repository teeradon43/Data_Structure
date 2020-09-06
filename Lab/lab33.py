# """
# Chapter : 4 - item : 3 - Secret Message
#  ส่งมาแล้ว 0 ครั้ง
# จงเขียน ฟังก์ชั่นสำหรับการ encode และ decode ของ String ที่รับมาโดยให้ทำเป็นรูปแบบ Queue

# รูปแบบการรับ Input โดยจะคั่นแต่ละตำแหน่งด้วย คอมม่า(',') :
#     - ตำแหน่งที่หนึ่ง string ไม่จำกัดความยาวโดยที่จะไม่นับช่องว่าง(spacebar)
#     - ตำแหน่งที่สอง ชุดตัวเลข(1-9)

# โดยที่รูปแบบการ encode คือ การนำ String ที่รับมาเพิ่มค่า ascii เท่ากับค่าของชุดตัวเลขในตำแหน่งแรก
# หลังจากนั้นให้ dequeue ชุดตัวเลขออกไปไว้ข้างหลังสุด เช่น ตัวอักษรตำแหน่งแรกคือ i และชุดตัวเลขในตำแหน่งแรกคือ 2 ดังนั้นตัวอักษรที่ได้จากการ 
# encode คือ k โดยจะทำการวนชุดตัวเลขไปเรื่อยๆจนกระทั่งทำการ encode ทุกตัวอักษรใน String ครบ ถ้าหากผลลัพธ์จากการเพิ่มหรือลดค่า ascii 
# ไม่ใช่ตัวอักษรให้กลับมาวนในชุดตัวอักษร เช่น อักษร z ทำการ encode ด้วยเลข 2 จะได้ b และหากทำการ decode ตัวอักษร A ด้วย 2 จะได้ Y 

# โดยการ decode หลังจาก encode ต้องให้คำตอบที่มีค่าเท่ากับ String เดิมก่อนทำการ encode 

# ***ให้ใช้วิธี enqueue และ dequeue ในการเลื่อนตำแหน่ง เท่านั้น***

# โดยรูปแบบการ run ดังนี้ :

# q1 = Queue(string)
# q2 = Queue(number)
# encodemsg(q1, q2)
# decodemsg(q1, q2)
# """
# class Queue:
#     def __init__(self,item = None):
#         self.item = []
#         if item != None:
#             for i in item:
#                 if i == ' ':
#                     continue
#                 self.item.append(i)

#     def enqueue(self,item):
#         self.item.append(item)

#     def dequeue(self):
#         if self.size() > 0:
#             return self.item.pop(0)

#     def size(self):
#         return len(self.item)

# def encodemsg(a,b):
#     pass
# def decodemsg(a,b):
#     pass


# Str,Num = input('Enter String and Code : ').split(',')
# sQ = Queue(Str) #Queue String
# nQ = Queue(Num) #Queue Number
# eQ = Queue() #encode queue
# dQ = Queue() #decode queue
# # print(nQ.item)
# while sQ.size() > 0:
#     t = sQ.dequeue()
#     n = ord(t)
#     dQ.enqueue(t)
#     d = int(nQ.dequeue())
#     n += d
#     if t >= 'A' and t <= 'Z':
#         if n > 90:
#             n -= 26
#     elif t >= 'a' and t <= 'z':
#         if n > 122:
#             n -= 26
#     eQ.enqueue(chr(n))
#     nQ.enqueue(d)

# print('Encode message is : ',eQ.item)
# print('Decode message is : ',dQ.item)

a = b = c = 1
b=2
print(a==b==c)