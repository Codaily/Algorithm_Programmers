def solution(N, stages):

    failure = {}
    cnt = 0 
    stages = sorted(stages)
    for i in range(1,N+1):
        cnt = 0
        for j in stages:
            if i == j:
                cnt += 1
            else :
                break  
        try:
            failure[i] = cnt/len(stages) 
        except ZeroDivisionError as e:
            failure[i] = 0
        del stages[:cnt]
    
    answer = sorted(failure.items(), key=lambda x: x[1],reverse=True)
    return [i[0] for i in answer]

print(solution(5,[1,2,2,1,3]))