def solution(s):
    answer = []
    strIdxs = {}
    for i in range(len(s)):
        if s[i] in strIdxs:
            answer.append(i - strIdxs[s[i]])
        else:
            answer.append(-1)
        
        strIdxs[s[i]] = i
    return answer
