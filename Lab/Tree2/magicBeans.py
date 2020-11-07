"""
Chapter : 8 - item : 1 - ถั่ววิเศษ
 ส่งมาแล้ว 0 ครั้ง
กฤษฎาได้ค้นพบเม็ดถั่ววิเศษที่เมื่อโยนลงดินแล้วถั่วจะสามารถเติบโตขึ้นและกลายเป็น Binary Search Tree (BST) ได้ 
โดยงานของนักศึกษาก็คือนักศึกษาจะต้องสร้าง BST ตามลำดับของข้อมูลนำเข้าซึ่งเป็นตัวเลขจำนวนเต็มที่ไม่ซ้ำกันเลย 
โดยในการใส่ค่าในแต่ละครั้งจะกลับมาที่ Root of BST เสมอ  แล้วท่องต้นไม้ไปทางซ้ายด้วยคำสั่ง "L" 
หรือท่องต้นไม้ไปทางขวาด้วยคำสั่ง "R" จนกว่าจะถึงตำแหน่งที่เหมาะสมที่จะใส่ข้อมูลแล้วจึงพิมพ์ "*" เพื่อใส่ข้อมูลลงไปในต้นไม้  

จงเขียนโปรแกรมเพื่อแสดงคำสั่งการท่องต้นไม้ในการใส่ข้อมูลทีละค่าตามลำดับของข้อมูลนำเข้า

Testcase : #1 1
Enter Input : 1 2 5 4 3 -2 -1
*
R*
RR*
RRL*
RRLL*
L*
LR*

Testcase : #2 6
Enter Input : 48 47 194194 3534 39 20 2014 35289 53
*
L*
R*
RL*
LL*
LLL*
RLL*
RLR*
RLLL*


"""

class Node:

    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    
    def __init__(self):
        self.root = None

    def insert(self,data):
        p = Node(data)
        res = ""
        if self.root == None:
            self.root = p
        else:
            r = self.root
            while True:
                if int(p.data) < int(r.data):
                    res+='L'
                    if r.left == None:
                        r.left = p
                        break
                    r = r.left
                else:
                    res+='R'
                    if r.right == None:
                        r.right = p
                        break
                    r = r.right
        print(res+'*')
        return self.root

if __name__ == '__main__':
    T = BST()
    inp = input('Enter Input : ').split()
    for i in inp:
        T.insert(i)
    

