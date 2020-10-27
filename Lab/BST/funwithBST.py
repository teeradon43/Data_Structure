"""
Chapter : 7 - item : 4 - สนุกไปกับ Binary Search Tree
 ส่งมาแล้ว 0 ครั้ง
ให้น้องรับ input เข้ามาและสร้าง Binary Search Tree ต่อมาให้แสดงผลแบบ Preorder , Inorder , Postorder และ Breadth First Search ตามลำดับ

Testcase : #1 1
Enter Input : 10 4 20 1 5
Preorder : 10 4 1 5 20 
Inorder : 1 4 5 10 20 
Postorder : 1 5 4 20 10 
Breadth : 10 4 20 1 5 

Testcase : #2 2
Enter Input : 0 -50 50 25 -25 13 -13 28 -38 75 -75 62 -62 100 -100
Preorder : 0 -50 -75 -100 -62 -25 -38 -13 50 25 13 28 75 62 100 
Inorder : -100 -75 -62 -50 -38 -25 -13 0 13 25 28 50 62 75 100 
Postorder : -100 -62 -75 -38 -13 -25 -50 13 28 25 62 100 75 50 0 
Breadth : 0 -50 50 -75 -25 25 75 -100 -62 -38 -13 13 28 62 100 

"""
class Queue:
    def __init__(self):
        self.data = []

    def dequeue(self):
        if not self.isEmpty():
            return self.data.pop(0)
        else:
            return 0

    def enqueue(self,i):
        self.data.append(i)

    def isEmpty(self):
        return self.data == []

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
        self.inL = []
        self.preL = []
        self.posL = []
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
    
    def Preorder(self, root):
        if root == None:
            return 0
        else:
            p = (root.data)
            return (self.preL.append(int(p)),self.Preorder(root.left),self.Preorder(root.right))

    def Inorder(self, root):
        if root == None:
            return 0
        else:
            p = (root.data)
            return (self.Inorder(root.left),self.inL.append(int(p)),self.Inorder(root.right))
    
    def Postorder(self, root):
        if root == None:
            return 0
        else:
            p = (root.data)
            return (self.Postorder(root.left),self.Postorder(root.right),self.posL.append(int(p)))

    def BreadthFS(self, root):
        q = Queue()
        q.enqueue(self.root)
        s = "Breadth : "
        while not q.isEmpty():
            node = q.dequeue()
            s += str(node.data) + ' '
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return s
            


if __name__ == '__main__':
    T = BST()
    inp = input('Enter Input : ').split()
    for i in inp:
        root = T.insert(i)
    T.Preorder(root)
    T.Inorder(root)
    T.Postorder(root)
    print('Preorder : ',end='')
    for i in T.preL:
        print(i, end = " ")
    print()
    print('Inorder : ',end='')
    for i in T.inL:
        print(i, end = " ")
    print()
    print('Postorder : ',end='')
    for i in T.posL:
        print(i, end = " ")
    print()
    print(T.BreadthFS(root))