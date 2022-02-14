from collections import Counter

def solution(str1, str2):

    sCount1 = Counter([str1[i:i+2].upper() for i in range(len(str1)-1) if str1[i].isalpha() and str1[i+1].isalpha()])
    sCount2 = Counter([str2[i:i+2].upper() for i in range(len(str2)-1) if str2[i].isalpha() and str2[i+1].isalpha()])
    intersaction = sCount1 & sCount2
    union = sCount1 | sCount2

    if intersaction == union :
        return 1 * 65536
    answer = sum(intersaction.values()) / sum(union.values()) * 65536
    return int(answer)