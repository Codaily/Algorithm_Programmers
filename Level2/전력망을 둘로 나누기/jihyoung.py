from collections import deque

def bfs(start, visited, graph):
    queue = deque([start])
    result = 1
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                result += 1
                queue.append(i)
                visited[i] = True

    return result

def solution(n, wires):
    answer = n

    # 인접 리스트 만들기 https://velog.io/@gndan4/DFSBFS
    graph = [[] for _ in range(n+1)]
    
    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    # 연결 끊고 개수 확인하기
    for start, not_visit in wires:
        print(start, not_visit)
        visitied = [False]*(n+1)
        visitied[not_visit] = True
        result = bfs(start,visitied, graph)

        # 개수가 비슷한지 확인
        if abs(result - (n-result)) < answer:
            answer = abs(result - (n-result))


    return answer



print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))


# https://freedeveloper.tistory.com/373