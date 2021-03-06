"""
Chapter : 8 - item : 2 - AVL ( Insert Only )
 ส่งมาแล้ว 0 ครั้ง
ให้น้องๆสร้าง AVL Tree ด้วย Class โดยผลลัพธ์ให้แสดงเป็น Tree ในแต่ละรอบหลังจาก Insert และปรับ Balance เรียบร้อยแล้ว


** ถ้าสงสัยสามารถดู visualization ของ AVL ได้ที่ website นี้ : https://www.cs.usfca.edu/~galles/visualization/AVLtree.html

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class AVL:

    ?????

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    ?????

Testcase : #1 1
Enter Input : 50 40 35 30 20 10 5
Insert : ( 50 )
 50
--------------------------------------------------
Insert : ( 40 )
 50
      40
--------------------------------------------------
Insert : ( 35 )
      50
 40
      35
--------------------------------------------------
Insert : ( 30 )
      50
 40
      35
           30
--------------------------------------------------
Insert : ( 20 )
      50
 40
           35
      30
           20
--------------------------------------------------
Insert : ( 10 )
           50
      40
           35
 30
      20
           10
--------------------------------------------------
Insert : ( 5 )
           50
      40
           35
 30
           20
      10
           5
--------------------------------------------------

Testcase : #2 2
Enter Input : 40 20 10 25 30 22 50
Insert : ( 40 )
 40
--------------------------------------------------
Insert : ( 20 )
 40
      20
--------------------------------------------------
Insert : ( 10 )
      40
 20
      10
--------------------------------------------------
Insert : ( 25 )
      40
           25
 20
      10
--------------------------------------------------
Insert : ( 30 )
           40
      30
           25
 20
      10
--------------------------------------------------
Insert : ( 22 )
           40
      30
 25
           22
      20
           10
--------------------------------------------------
Insert : ( 50 )
           50
      40
           30
 25
           22
      20
           10
--------------------------------------------------

Testcase : #3 3
Enter Input : 30 20 10
Insert : ( 30 )
 30
--------------------------------------------------
Insert : ( 20 )
 30
      20
--------------------------------------------------
Insert : ( 10 )
      30
 20
      10
--------------------------------------------------

Testcase : #4 4
Enter Input : 30 10 20
Insert : ( 30 )
 30
--------------------------------------------------
Insert : ( 10 )
 30
      10
--------------------------------------------------
Insert : ( 20 )
      30
 20
      10
--------------------------------------------------

Testcase : #5 5
Enter Input : 30 40 10 50 20 5 35
Insert : ( 30 )
 30
--------------------------------------------------
Insert : ( 40 )
      40
 30
--------------------------------------------------
Insert : ( 10 )
      40
 30
      10
--------------------------------------------------
Insert : ( 50 )
           50
      40
 30
      10
--------------------------------------------------
Insert : ( 20 )
           50
      40
 30
           20
      10
--------------------------------------------------
Insert : ( 5 )
           50
      40
 30
           20
      10
           5
--------------------------------------------------
Insert : ( 35 )
           50
      40
           35
 30
           20
      10
           5
--------------------------------------------------

Testcase : #6 6
Enter Input : 5 5 5 5 5 5 5 5 5 5 5
Insert : ( 5 )
 5
--------------------------------------------------
Insert : ( 5 )
      5
 5
--------------------------------------------------
Insert : ( 5 )
      5
 5
      5
--------------------------------------------------
Insert : ( 5 )
           5
      5
 5
      5
--------------------------------------------------
Insert : ( 5 )
           5
      5
           5
 5
      5
--------------------------------------------------
Insert : ( 5 )
           5
      5
 5
           5
      5
           5
--------------------------------------------------
Insert : ( 5 )
           5
      5
           5
 5
           5
      5
           5
--------------------------------------------------
Insert : ( 5 )
                5
           5
      5
           5
 5
           5
      5
           5
--------------------------------------------------
Insert : ( 5 )
                5
           5
                5
      5
           5
 5
           5
      5
           5
--------------------------------------------------
Insert : ( 5 )
                5
           5
      5
                5
           5
                5
 5
           5
      5
           5
--------------------------------------------------
Insert : ( 5 )
                5
           5
                5
      5
                5
           5
                5
 5
           5
      5
           5
--------------------------------------------------

Testcase : #7 9
Enter Input : 500 5000 499 498 497 499 497
Insert : ( 500 )
 500
--------------------------------------------------
Insert : ( 5000 )
      5000
 500
--------------------------------------------------
Insert : ( 499 )
      5000
 500
      499
--------------------------------------------------
Insert : ( 498 )
      5000
 500
      499
           498
--------------------------------------------------
Insert : ( 497 )
      5000
 500
           499
      498
           497
--------------------------------------------------
Insert : ( 499 )
           5000
      500
           499
 499
      498
           497
--------------------------------------------------
Insert : ( 497 )
           5000
      500
           499
 499
           498
      497
           497
--------------------------------------------------


"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class AVL:

     def __init__(self):
          # code here
          pass

     def printTree(self, node, level = 0):
          if node != None:
               self.printTree(node.right, level + 1)
               print('     ' * level, node)
               self.printTree(node.left, level + 1)

    # code here