def makeMultipleSet(origin):
    mulSet = []
    for i in range(0, len(origin)-1):
        new = origin[i] + origin[i+1]
        if new.isalpha():
            mulSet.append(new)

    return mulSet

def countIntersectionElement(set1, set2):
    result = []
    for i in set2:
        if i in set1:
            set1.remove(i)
            result.append(i)

    return len(result)

def countUnionElement(set1, set2):
    result = set1.copy()
    temp = set1.copy()
    for i in set2:
        if i not in temp:
            result.append(i)
        else:
            temp.remove(i)

    return len(result)

def J(cntInt, cntU):

    if cntU == 0 :
        return 65536

    return int((cntInt / cntU) * 65536)

def solution(str1, str2):
    
    return J(countIntersectionElement(makeMultipleSet(str1.lower()), makeMultipleSet(str2.lower())), countUnionElement(makeMultipleSet(str1.lower()), makeMultipleSet(str2.lower())))

print(solution("aaaa", "aaaa"))