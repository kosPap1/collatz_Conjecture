def evenOddNum(x):
    e = 0
    o = 0
    for i in range(len(x)):
        if (x[i] % 2) == 0:
            e += 1
        elif (x[i] % 2) != 0:
            o += 1
    return [e, o]