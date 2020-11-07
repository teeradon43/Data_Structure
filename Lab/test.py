class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()
    
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,i):
        self.items.append(i)
    
    def dequeue(self):
        return self.items.pop(0)

def sort(l):
    s = Stack()
    n = len(l)
    for i in range(n):
        print('run0')
        max = l[0]
        min = l[0]
        for j in range(0,len(l)):
            print('run1')
            if l[j] > max:
                max = l[j]
            elif l[j] < min:
                min = l[j]
        
        s.push(max)
        l.remove(max)
    while s.items != []:
        l.append(s.pop())
    return l

if __name__ == '__main__':
    l = [5,4,3,2,1]
    print(sort(l))