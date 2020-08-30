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
s2 = Stack()
txt = input('Enter Input : ').split(',')
for i in txt:
    chr = i.split()
    if chr[0] == 'A':
        # while not s.isEmpty():
        #     if int(s.peek()) <= int(chr[-1]):
        #         s.pop()
        #     else:
        #         break
        s.push(chr[-1])
    elif chr[0] == 'S':
        while not s.isEmpty():
            if int(s.peek()) % 2 == 1:
                s2.push(int(s.pop())+2)
            else:
                s2.push(int(s.pop())-1)
        while not s2.isEmpty():
            while not s.isEmpty():
                if int(s.peek()) <= int(s2.peek()):
                    s.pop()
                else:
                    break
            s.push(s2.pop())
    else:
        count = 0
        while not s.isEmpty():
            if not s2.isEmpty():
                if int(s.peek()) >= int(s2.peek()):
                    count += 1
                    s2.push(s.pop())
                else:
                    break
            else:
                s2.push(s.pop())
                count += 1
        while not s2.isEmpty():
            s.push(s2.pop())

        print(count)