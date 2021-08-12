def solution(n, lost, reserve):
    arr = set(lost+reserve)
    flost = list(arr-set(reserve))
    freserve = list(arr - set(lost))

    for i in range(len(flost)):
        for j in range(len(freserve)):
            if flost[i] + 1 == freserve[j] or flost[i]- 1 == freserve[j] :
                flost[i] = -1
                freserve[j] = -1
                break
    return n - (len(flost)-flost.count(-1))