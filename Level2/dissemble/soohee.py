def minus(kind):
    
    for i in range(1,len(kind)):
        sum = 0
        for j in range(0,i):
            sum += kind[j]
        kind[i] -=sum
    return kind

def solution(clothes):

    clothes.sort(key=lambda x:x[1])
    print(clothes)
    clo = clothes[0][1]
    kind = [] 
    flag = 0

    for i in range(len(clothes)):
        if clo != clothes[i][1]:
            kind.append(i+1)
            clo = clothes[i][1]        
        else:
            flag += 1
    print(kind)
    if flag == len(clothes):
        answer = len(clothes) + 1
    else :            
        minus(kind) 
        answer = kind[0] + 1
        for i in range(1,len(kind)):
            answer *= (kind[i]+1) 
       
    print(answer)
    return answer-1 

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"],["blue_shirt","shirt"],["red_jeans","jeans"]])