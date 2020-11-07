def bubble_sort(lst,index,n):
    if n == 1:
        return lst
    if index == n-1:
        return bubble_sort(lst,0,n-1)
    if lst[index] < 0 :
        return bubble_sort(lst,index+1,n)
    next_index = index+1
    while lst[next_index] < 0 and next_index < n-1:
        next_index += 1
    
    if lst[index] > lst[next_index] and lst[next_index]>=0:
        lst[index], lst[next_index] = lst[next_index], lst[index]
    
    return bubble_sort(lst,index+1,n)

if __name__ == '__main__':
    inp = [int(x) for x in input('Enter Input : ').split()]
    inp = bubble_sort(inp,0,len(inp))
    for i in inp:
        print(i,end = ' ')