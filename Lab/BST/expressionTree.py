"""
Chapter : 7 - item : 5 - Expression Tree
 ส่งมาแล้ว 0 ครั้ง
ให้น้องๆรับ input เป็น postfix จากนั้นให้แปลงเป็น Expression Tree , Infix และ Prefix  โดย Operator จะมีแค่ + - * /

Testcase : #1 1
Enter Postfix : ab+cde+**
Tree :
                e
           +
                d
      *
           c
 *
           b
      +
           a
--------------------------------------------------
Infix : ((a+b)*(c*(d+e)))
Prefix : *+ab*c+de

Testcase : #2 2
Enter Postfix : abc*+de*f+g*+
Tree :
           g
      *
                f
           +
                     e
                *
                     d
 +
                c
           *
                b
      +
           a
--------------------------------------------------
Infix : ((a+(b*c))+(((d*e)+f)*g))
Prefix : ++a*bc*+*defg

Testcase : #3 3
Enter Postfix : ab+c*de-fg+*-
Tree :
                g
           +
                f
      *
                e
           -
                d
 -
           c
      *
                b
           +
                a
--------------------------------------------------
Infix : (((a+b)*c)-((d-e)*(f+g)))
Prefix : -*+abc*-de+fg

"""
class Stack:
     def __init__(self):
          self.items = []
     def push(self, i):
          self.items.append(i)
     def pop(self):
          if self.items != []:
               return self.items.pop(-1)
     def isEmpty(self):
          return self.items == []
     def __str__(self):
          res = ''
          while(not self.isEmpty()):
               res = str(self.pop()) + res
          return res
          
class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.preL = []
        self.posL = []
        self.inL = []
        self.breL = []
        
    def insert(self,data):
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
    
    def pre_order(self, node):
        if node == None:
            return ''
        s = str(node.data)\
            + self.pre_order(node.left)\
                + self.pre_order(node.right)
        return s

    def in_order(self, node):
        if node == None:
            return ''
        s = self.in_order(node.left)\
             + str(node.data)\
                 + self.in_order(node.right)
        if node.left is not None and node.right is not None:
            s = '(' + s + ')'
        return s

if __name__ == '__main__':
     T = BST()
     s = Stack()
     inp = input('Enter Postfix : ')
     for i in inp:
          if i in '+-*/':
               op1 = s.pop()
               op2 = s.pop()
               s.push(Node(i,op2,op1))
          else:
               s.push(Node(i))
     root = s.pop()
     print('Tree :')
     T.printTree(root)
     print('--------------------------------------------------')
     print('Infix :',T.in_order(root))
     print('Prefix :',T.pre_order(root))
     
          