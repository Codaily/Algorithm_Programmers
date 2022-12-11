def solution(k, tangerine):
    answer = 0
    dict = {}
    for t in tangerine:
        if t in dict:
            dict[t] += 1
        else:
            dict[t] = 1
    
    dict = sorted(dict.items(), key = lambda x: x[1],reverse=True)
    
    for _, v in dict:
        if k <= 0 :
            return answer
        else:
            answer += 1
            k -= v
    return answer
