"""
Item 4 - Perket by Qiral

(Test cases)
input : 3 10
output : 7

input : 3 8,5 8
output : 1

input : 1 7,2 6,3 8,4 9
output : 1
"""

def solveFormular(List,index,count):
    if count == 0:
        return 1, 0
    s, b = solveFormular(List, index + 1, count // 2)

    if count % 2 == 1:
        s *= int(List[index].split()[0]);
        b += int(List[index].split()[1]);
    
    return s, b

if __name__ == '__main__':
    #Main
    inp = input("Enter Input : ").split(',')
    diff = None
    for i in range(1,2**len(inp)):
        res1, res2 = solveFormular(inp,0,i)
        res = abs(res1-res2)
        if diff == None or res < diff:
            diff = res
    print(diff)