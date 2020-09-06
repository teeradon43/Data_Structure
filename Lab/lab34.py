"""
Chapter : 4 - item : 4 - เดาใจไว้แล้วว่าเธอรักฉันแบบที่ฉันรัก
สมมติว่านักศึกษาแอบชอบคนๆหนึ่งอยู่ โดยที่นักศึกษาและคนๆนั้นจะมีกิจกรรมและสถานที่ที่ไปแตกต่างกันในแต่ละวัน
ให้นักศึกษาเขียนโปรแกรมที่จะหาว่าสิ่งที่นักศึกษาและคนๆนั้นทำในแต่ละวันจะทำให้ได้คบกันหรือไม่ โดยใช้ Queue

กิจกรรม                           สถานที่
0 = กินข้าว(Eat)                   0 = ร้านอาหาร(Res.)
1 = เล่นเกม(Game)                  1 = ห้องเรียน(ClassR.)
2 = ทำโจทย์ datastruc(Learn)      2 = ห้างสรรพสินค้า(SuperM.)
3 = ดูหนัง(Movie)                  3 = บ้าน(Home)

โดยการรับ Input จะประกอบด้วย
กิจกรรม:สถานที่(ของนักศึกษาและของคนๆนั้น) โดยในแต่ละวันจะคั่นด้วยเครื่องหมาย ,

เช่น วันที่ 1 นักศึกษาไปกินข้าวที่ร้านอาหาร และ คนๆนั้นไปนั่งทำโจทย์ datastruc ที่ร้านอาหาร 
       วันที่ 2 นักศึกษาไปเล่นเกมที่บ้าน และ คนๆนั้นไปดูหนังที่ห้างสรรพสินค้า
จะได้ว่า 0:0 2:0,1:3 3:2

***มีการคิดคะแนนดังนี้***
·       กิจกรรมเดียวกันแต่คนละสถานที่       +1
·       สถานที่เดียวกันแต่ทำกิจกรรมต่างกัน    +2
·       กิจกรรมเดียวกันและสถานที่เดียวกัน     +4
·       ไม่เหมือนกันเลย                   -5
หากมีคะแนนมากกว่าหรือเท่ากับ 7 จะถือว่าได้คบกัน แต่ถ้าคะแนนน้อยกว่า 7 แต่มากกว่า 0 เป็นคนคุย น้อยกว่านั้นถือว่าเป็นได้แค่เพื่อน
โดยในแต่ละขั้นตอนให้แสดงผลดังตัวอย่าง
"""

class Queue:
    def __init__(self,item = None):
        self.item = []
        if item != None:
            for i in item:
                if i == ' ':
                    continue
                self.item.append(i)

    def enqueue(self,item):
        self.item.append(item)

    def dequeue(self):
        if self.size() > 0:
            return self.item.pop(0)

    def size(self):
        return len(self.item)

event = {
    "0":"Eat",
    "1":"Game",
    "2":"Learn",
    "3":"Movie"
}
place = {
    "0":"Res.",
    "1":"ClassR.",
    "2":"SuperM.",
    "3":"Home"
}
mQ = Queue()
yQ = Queue()
txt = input('Enter Input : ').split(',')
res = ''
mL = 'My   Queue = '
yL = 'Your Queue = '
mA = 'My   Activity:Location = '
yA = 'Your Activity:Location = '
score = 0
count = 0
for i in txt:
    j = i.split(' ')
    mQ.enqueue(j[0])
    yQ.enqueue(j[1])

while mQ.size() > 0:
    a = mQ.dequeue()
    b = yQ.dequeue()
    if count > 0:
        mL += ', '
        yL += ', '
        mA += ', '
        yA += ', '
    mL += a
    yL += b
    mA += event[a[0]] + ':' + place[a[-1]]
    yA += event[b[0]] + ':' + place[b[-1]]
    if a == b:
        score += 4
    elif a[0] == b[0]:
        score += 1
    elif a[-1] == b[-1]:
        score += 2
    else:
        score -= 5
    count += 1
    

print(mL)
print(yL)
print(mA)
print(yA)

if score > 6:
    res += "Yes! You're my love! "
elif score > 0:
    res += "Umm.. It's complicated relationship! "
else:
    res += "No! We're just friends. "
res += ': Score is '
res += str(score)
res += '.'
print(res)