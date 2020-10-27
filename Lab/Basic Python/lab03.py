print('*** New Range ***')
rng = [item for item in input('Enter Input : ').split()]
tu = []
i = 0
if len(rng) == 3:
    i = float(rng[0])
    while i < float(rng[1]):
        tu.append(round(float(i), 3))
        i = i + float(rng[2])

elif len(rng) == 2:
    i = float(rng[0])
    while i < float(rng[1]):
        tu.append(float(i))
        i = i + 1

else:
    while i < float(rng[0]):
        tu.append(float(i))
        i = i + 1

print(tuple(tu))