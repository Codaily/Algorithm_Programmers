def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i] == False:
            dfs(n, i , computers, visited)
    answer += 1

    return answer

def dfs(n, param_idx, computers, v):
    v[param_idx] = True
    for dfs_idx in range(n):
        if v[dfs_idx] == False and computers[param_idx][dfs_idx] == 1:
            dfs(n, dfs_idx, computers, v)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
