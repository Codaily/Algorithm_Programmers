visited = []
def dfs(start,com):
    global visited
    stack = [start]
    while stack:
        s = stack.pop()       
        visited[s]=1
        for i in range(0, len(com)):
            if com[s][i] ==1 and visited[i] == 0:
                stack.append(i)
                    
def solution(n, computers):
    global visited
    visited = [0] * n
    answer = 0
    for i in range(n):
        if visited[i] == 0:
            dfs(i,computers)
            answer += 1

    return answer
print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]))