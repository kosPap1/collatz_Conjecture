def digitClass(x):
    z1 = 0
    z2 = 0
    z3 = 0
    z4 = 0
    z5 = 0
    z6 = 0
    z7 = 0
    z8 = 0
    z9 = 0

    for i in range(len(x)):
        t = x[i]
        tempList = []
        for a in str(t):
            tempList.append(int(a))
        if tempList[0] == 1:
            z1 += 1
        if tempList[0] == 2:
            z2 += 1
        if tempList[0] == 3:
            z3 += 1
        if tempList[0] == 4:
            z4 += 1
        if tempList[0] == 5:
            z5 += 1
        if tempList[0] == 6:
            z6 += 1
        if tempList[0] == 7:
            z7 += 1
        if tempList[0] == 8:
            z8 += 1
        if tempList[0] == 9:
            z9 += 1
    resultClassList = [z1, z2, z3, z4, z5, z6, z7, z8, z9]
    return resultClassList