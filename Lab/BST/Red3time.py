"""
ให้น้องๆรับ input เป็น list และ k โดยให้สร้าง Binary Search Tree จาก list ที่รับมา 
และหลังจากนั้นให้ทำการดูว่าใน Tree มีค่าไหนที่มากกว่าค่า k หรือไม่ ถ้ามีให้ทำการคูณ 3 เพิ่มเข้าไป

Testcase : #1 1
Enter Input : 67 102 81 35 15 7 99 196 202 152/90
                202
           196
                152
      102
                99
           81
 67
      35
           15
                7
--------------------------------------------------
                606
           588
                456
      306
                297
           81
 67
      35
           15
                7

Testcase : #2 2
Enter Input : 5 3 -1 4 7 6 8/-5
           8
      7
           6
 5
           4
      3
           -1
--------------------------------------------------
           24
      21
           18
 15
           12
      9
           -3

Testcase : #3 3
Enter Input : 5 3 1 4 7 6 8/4
           8
      7
           6
 5
           4
      3
           1
--------------------------------------------------
           24
      21
           18
 15
           4
      3
           1


"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.ans = []

    def insert(self, data):
        p = Node(data)
        if self.root == None:
            self.root = p
        else:
            r = self.root
            while True:
                if int(p.data) < int(r.data):
                    if r.left == None:
                        r.left = p
                        break
                    r = r.left
                else:
                    if r.right == None:
                        r.right = p
                        break
                    r = r.right
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
        
    def findBelow(self, value, root):
        if root == None:
            return 0
        else:
            p = (root.data)
            if int(p) < int(value):
                return ((self.findBelow(value, root.left)), self.ans.append(int(p)) , (self.findBelow(value, root.right)))
            else:
                return (self.findBelow(value, root.left))
     
    def findUpper(self, value, root):
        if root == None:
            return 0
        else:
            p = (root.data)
            if int(p) > int(value):
                 root.data = int(root.data) * 3
                 return ((self.findUpper(value, root.left)), self.ans.append(int(p)) , (self.findUpper(value, root.right)))
            else:
                return (self.findUpper(value, root.right))
            
if __name__ == '__main__':
     T = BST()
     inp = input('Enter Input : ')
     inp = inp.replace('/',' ')
     inp = list(inp.split())
     for i in range(0,len(inp)-1):
          root = T.insert(inp[i])
     T.printTree(root)
     print("--------------------------------------------------")
     T.findUpper(inp[-1],root)
     T.printTree(root)