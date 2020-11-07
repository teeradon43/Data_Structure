def bubble_sort(lst,index,n):
    if n == 1:
        return lst
    if index == n-1:
        return bubble_sort(lst,0,n-1)
    
    if lst[index] > lst[index+1]:
        lst[index], lst[index+1] = lst[index+1], lst[index]
        
    return bubble_sort(lst,index+1,n)

if __name__ == '__main__':
    inp = input('Enter Input : ')
    l = []
    for i in inp:
        l.append(int(i))
    l = bubble_sort(l,0,len(l))
    l_2 = set(l)
    repeat = False
    if len(l) != len(l_2):
        repeat = True
    res = ''
    for i in l:
        res += str(i)
    if len(l_2) == 1:
        print('Repdrome')
    elif res == inp and repeat == False:
        print('Metadrome')
    elif res == inp and repeat == True:
        print('Plaindrome')
    elif res == inp[::-1] and repeat == False:
        print('Katadrome')
    elif res == inp[::-1] and repeat == True:
        print('Nialpdrome')
    else:
        print('Nondrome')