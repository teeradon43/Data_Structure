def bubble_sort(lst,index,n):
    if n == 1:
        return lst
    if index == n-1:
        return bubble_sort(lst,0,n-1)
    
    if lst[index] > lst[index+1]:
        lst[index], lst[index+1] = lst[index+1], lst[index]
        
    return bubble_sort(lst,index+1,n)

if __name__ == '__main__':
    inp = [int(x) for x in input('Enter Input : ').split()]
    inp = bubble_sort(inp,0,len(inp))
    print(inp)