'''
 * กลุ่มที่  : 20010102
 * 62010436 ธีรดนย์ จันทร์หอม
 * chapter : 15	item : 1	ครั้งที่ : 0002
 * Assigned : Friday 21st of August 2020 09:49:04 AM --> Submission : Friday 21st of August 2020 09:55:10 AM	
 * Elapsed time : 6 minutes.
 * filename : exam1_1.py
'''
print(' *** Wind classification ***')
spd = float(input('Enter wind speed (km/h) : '))

res = ''
if spd >= 209:
    res = 'Super Typhoon.'
elif spd >= 102:
    res = 'Typhoon.'
elif spd >= 56:
    res = 'Tropical Storm.'
elif spd >= 52:
    res = 'Depression.'
elif spd >= 0:
    res = 'Breeze.'
else: print("!!!Wrong value can't classify.")

if res != '' : print('Wind classification is',res)

#============================================

'''
 * กลุ่มที่  : 20010102
 * 62010436 ธีรดนย์ จันทร์หอม
 * chapter : 15	item : 2	ครั้งที่ : 0002
 * Assigned : Friday 21st of August 2020 09:55:19 AM --> Submission : Friday 21st of August 2020 10:01:24 AM	
 * Elapsed time : 6 minutes.
 * filename : exam1_2.py
'''
print(' *** Divisible number ***')
num = int(input('Enter a positive number : '))
if num < 1:
    print(num,'is OUT of range !!!')
else:
    count = 0
    print('Output ==> ', end='')
    for i in range(1,num+1):
        if num % i == 0:
            print(i,end=' ')
            count += 1
    print()
    print('Total ==>',count)

    #========================================================================

'''
 * กลุ่มที่  : 20010102
 * 62010436 ธีรดนย์ จันทร์หอม
 * chapter : 15	item : 3	ครั้งที่ : 0004
 * Assigned : Friday 21st of August 2020 10:01:32 AM --> Submission : Friday 21st of August 2020 11:35:05 AM	
 * Elapsed time : 93 minutes.
 * filename : exam1_3.py
'''
print(' *** String count ***')
txt = input('Enter message : ')
#65 is uppercase A
#97 is lowercase a
lower =[]
countL = 0
upper = []
countU = 0
for LOW in range(97,124):
    for i in range(len(txt)):
        if ord(txt[i]) == LOW:
            countL += 1
            if txt[i] in lower:
                pass
            else:
                lower.append(txt[i])
            
for UPP in range(65,92):
    for i in range(len(txt)):
        if ord(txt[i]) == UPP:
            countU += 1
            if txt[i] in upper:
                pass
            else:
                upper.append(txt[i])

print('No. of Upper case characters :',countU)
print('Unique Upper case characters : ',end='')
for i in range(len(upper)):
    print(upper[i],end='  ')
print()
print('No. of Lower case Characters :',countL)
print('Unique Lower case characters : ',end='')
for i in range(len(lower)):
    print(lower[i],end='  ')
print()

#=======================================================

'''
 * กลุ่มที่  : 20010102
 * 62010436 ธีรดนย์ จันทร์หอม
 * chapter : 15	item : 4	ครั้งที่ : 0002
 * Assigned : Friday 21st of August 2020 10:22:43 AM --> Submission : Friday 21st of August 2020 10:53:53 AM	
 * Elapsed time : 31 minutes.
 * filename : exam1_4.py
'''
# l1 = ['1','2','3']
# temp = l1[0]
# l1.pop(0)
# l1.append(temp)
# print(l1)

print('*** String Rotation ***')
l1,l2 = map(list,input('Enter 2 strings : ').split())
meml1 = [i for i in l1]
meml2 = [i for i in l2]
count = 0
while l1 != meml1 or l2 != meml2 or count == 0:
    temp1 = l1[-1]
    temp2 = l2[0]
    l1.pop()
    l2.pop(0)
    l1.insert(0,temp1)
    l2.append(temp2)
    count += 1
    if(count<=5):
        print(count,end=' ')
        for i in l1:
            print(i,end='')
        print(' ',end='')
        for i in l2:
            print(i,end='')
        print()
    else:
        if l1 == meml1 and l2 == meml2:
            if count==6:
                pass
            else:
                print(' . . . . . ')
            print(count,end=' ')
            for i in l1:
                print(i,end='')
            print(' ',end='')
            for i in l2:
                print(i,end='')
            print() 
print('Total of ',count,'rounds.')


#====================================


'''
 * กลุ่มที่  : 20010102
 * 62010436 ธีรดนย์ จันทร์หอม
 * chapter : 15	item : 5	ครั้งที่ : 0001
 * Assigned : Friday 21st of August 2020 10:53:57 AM --> Submission : Friday 21st of August 2020 11:33:11 AM	
 * Elapsed time : 39 minutes.
 * filename : exam1_5.py
'''
class MyInt:
    def __init__(self,num):
        self.num = num
        self.curNum = num

    def toRoman(self):
        roMan = ''
        while self.num > 0:
            if self.num >= 1000:
                roMan+='M'
                self.num -= 1000
            elif self.num >= 900:
                roMan+='CM'
                self.num -= 900
            elif self.num >= 500:
                roMan+='D'
                self.num -= 500
            elif self.num >= 400:
                roMan+='CD'
                self.num -= 400
            elif self.num >= 100:
                roMan+='C'
                self.num -= 100
            elif self.num >= 90:
                roMan+='XC'
                self.num -= 90
            elif self.num >= 50:
                roMan+='L'
                self.num -= 50
            elif self.num >= 40:
                roMan+='XL'
                self.num -= 40
            elif self.num >= 10:
                roMan+='X'
                self.num -= 10
            elif self.num >= 9:
                roMan+='IX'
                self.num -= 9
            elif self.num >= 5:
                roMan+='V'
                self.num -= 5
            elif self.num >= 4:
                roMan+='IV'
                self.num -= 4
            elif self.num >= 1:
                roMan+='I'
                self.num -= 1
        return roMan


    def __add__(self,b):
        self.sum = self.curNum + b.curNum
        return self.sum+(self.sum//2)

print(' *** class MyInt ***')
x,y = map(int,input('Enter 2 number : ').split())
a = MyInt(x)
b = MyInt(y)

print(x,'convert to Roman :',a.toRoman())
print(y,'convert to Roman :',b.toRoman())
print(x,'+',y,'=',a.__add__(b))