# from itertools import combinations
# def solution(n, costs):
#     answer = []

#     line = [i[2] for i in costs]
#     comLine = list(combinations(line, n-1))
#     for i in comLine:
#         answer.append(sum(i))
#     return min(answer)

def solution(n, costs):
    answer = 0
    #costs.sort()
    costs.sort(key=lambda x : x[2])
    line = [0]
    print(costs)
    while len(line) < n :
        for i in costs:
            if  i[0] in line and i[1] in line : #이미 들른부분
                continue
            if i[0] in line or i[1] in line:
                line+=[i[0],i[1]]
                line = list(set(line))
                answer += i[2]
                break
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))