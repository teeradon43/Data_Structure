def sort_alphabet(lst, char,index,n):
    if n == 1:
        return lst
    if index == n-1:
        return sort_alphabet(lst,char,0,n-1)
    
    if char[index] > char[index+1]:
        lst[index], lst[index+1] = lst[index+1], lst[index]
        char[index], char[index+1] = char[index+1], char[index]
        
    return sort_alphabet(lst,char,index+1,n)

if __name__ == '__main__':
    inp = input('Enter Input : ').split()
    a_li = [] # list of alphabet
    for word in inp:
        for char in word:
            if ord(char) > 96 and ord(char) < 123: # ascii in a to z
                a_li.append(ord(char))
                break
    res = sort_alphabet(inp,a_li,0,len(a_li))
    print(' '.join(res))