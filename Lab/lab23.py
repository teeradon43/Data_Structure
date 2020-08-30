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

inF = input('Enter Infix : ')
postF = ''
s = Stack()
for i in inF:
    if i in '()':
        if i == '(':
            s.push(i)
        else:
            while not s.isEmpty():
                if s.peek() != '(':
                    postF += s.pop()
                else:
                    s.pop()
                    break
    elif i == '^':
        s.push(i)
    elif i in '*/':
        if not s.isEmpty():
            if s.peek() in '*/^':
                postF += s.pop()
        s.push(i)
    elif i in '+-':
        while not s.isEmpty():
            if s.peek() in '+-*/' :
                postF += s.pop()
            else:
                break
        s.push(i)
    else:
        postF += i
while not s.isEmpty() :
    postF += s.pop()
print('Postfix :',postF)