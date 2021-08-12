def solution(d, budget):
    result = 0
    d = sorted(d)
    for i in d :
        if budget >= i :
            budget -= i
            result += 1 
    return result

print(solution([2,2,3,3],10))


    