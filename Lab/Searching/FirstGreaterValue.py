def first_greater_search(l, r, arr, arr2, x, v):
    
    if l == r:
        print('No First Greater Value')
        if(v<x):
            return first_greater_search(0,r,arr,arr2,x,v+1)
    elif arr[l] > arr2[v]:
        print(arr[l])
        if v < x:
            return first_greater_search(0,r,arr,arr2,x,v+1)
    else:
        return first_greater_search(l+1,r,arr,arr2,x,v)

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), list(map(int,inp[1].split()))
first_greater_search(0, len(arr) - 1, sorted(arr), sorted(k),len(k)-1,0)