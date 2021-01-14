def solution(clothes):

    dic = {}
    for i, j in clothes:
        if j not in dic:
            dic[j] =1
        else:
            dic[j]+=1
    
    answer = 1
    if dic.values()==3 :
        answer = len(clothes)
    else:
        for i in dic.values():
            answer *= (i + 1)

    return answer-1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"],["blue_shirt","shirt"],["red_jeans","jeans"]])