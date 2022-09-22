def trendRemove(x):
    det = []
    for i in range(0, len(x)):
        value = x[i] - x[i - 1]
        det.append(value)

    return det
