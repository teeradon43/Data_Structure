# item : 3 - ( 2^(input) ) - 1
# เขียน Recursive เพื่อหาว่าเลขตั้งแต่ 0 จนถึง ( 2^(input) ) - 1 นั้นมีตัวอะไรบ้าง
# ตัวอย่างเช่น ถ้าหาก input = 2 ก็ต้องแสดงผลลัพธ์เป็น 00 , 01 , 10 , 11
# หากเป็นเลขติดลบให้แสดงผลเป็น Only Positive & Zero Number ! ! ! 
def findValue(n):
    #do sth
    if n == 0:
        txt = '0'+str(inp)
        a = bin(0)[2:]
        print(a.zfill(inp))
        return 1
    else:
        print(bin(findValue(n-1))[2:].zfill(inp))
        return n+1

if __name__ == '__main__':
    global inp
    inp = int(input('Enter Number : '))
    if inp < 0:
        print('Only Positive & Zero Number ! ! !')
    else:
        findValue(2**inp-1)
        