myList = [c for c in input('Enter String : ')]

inde = []
res = []
for i in range(len(myList)):
    # if myList[i] in inde:
    #     res.index(myList[i]).append()
    # else:
    if myList[i] not in inde:
        inde.append(myList[i])
    res.append(inde.index(myList[i]))
print(res)