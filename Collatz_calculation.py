def collatzCalc(k):
    results = []
    while k != 1:
        if (k % 2) == 0:
            k = int(k / 2)
        elif (k % 2) != 0:
            k = (3 * k) + 1
        results.append(k)
    return results




