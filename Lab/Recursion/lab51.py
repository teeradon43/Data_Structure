def Min(list,n):
    if n == 1:
        return int(list[0])
    else:
        return int(list[n-1]) if int(list[n-1]) < Min(list,n-1) else Min(list,n-1)

inp = input('Enter Input : ').split(' ')
print('Min :',Min(inp,len(inp)))

# Min inp,6