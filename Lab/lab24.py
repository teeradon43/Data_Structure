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
txt = input('Enter Input : ').split(',')
for i in txt:
    chr = i.split()
    if chr[0] == 'A':
        while not s.isEmpty():
            if int(s.peek()) <= int(chr[-1]):
                s.pop()
            else:
                break
        s.push(chr[-1])
    else:
        print(s.size())