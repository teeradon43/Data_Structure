print(' *** New Range ***')

def findRange(strt=0,sTop=0,stP=1): #Start , Stop , Step
    if strt > sTop:
        strt , sTop = sTop , strt
    while strt < sTop:
        print(strt, end=' ')
        strt += stP
    pass

x = [float(i) for i in input('Enter Range : ').split()]
if len(x) < 3:
    for e in range(3):
        x.append(0) if len(x) == 1 else x.append(1)
findRange(x[0],x[1],x[2])