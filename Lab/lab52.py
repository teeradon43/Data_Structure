# ****ห้ามใช้คำสั่ง len, for, while, do while, split*****
sym = ['*','~']
n = -1
def length(txt):
    # Do
    global n 
    n += 1
    if txt=='':
        return ''
    else:
        return txt[:1]+sym[n%2]+length(txt[1:])

# print(length(input("Enter Input : ")),sep="")
print(length(input('Enter Input : ')))
print(n)