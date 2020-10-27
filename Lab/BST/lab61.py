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
            


T = BST()
inp = input('Enter Input : ')
inp = inp.replace('|',' ')
inp = list(inp.split())
for i in range(0,len(inp)-1):
    root = T.insert(inp[i])
T.printTree(root)
print('--------------------------------------------------')
print('Below',inp[-1],': ',end = '')
T.findBelow(inp[-1],root)
res = ''
for i in T.ans:
    res += str(i) + ' '
print('Not have' if res == '' else res)

"""
Enter Input : 4 10 2 1 3 7 -1 -4 9|5
      10
                9
           7
 4
           3
      2
           1
                -1
                     -4
--------------------------------------------------
Below 5 : -4 -1 1 2 3 4 
"""