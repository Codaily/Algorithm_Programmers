def solution(citations):
    H_index = len(citations)
    answer = 0
    while True:
        Hcnt , Lcnt = 0, 0 # H_index 보다 작거나 큰것의 개수
        for i in citations:
            if i >= H_index:
                Hcnt +=1
            else:
                Lcnt +=1 
        
        if Hcnt >= H_index:
            answer = H_index
            break
        else:
            H_index -=1

    print(answer)
    return answer

solution([2,2,2,2,2])