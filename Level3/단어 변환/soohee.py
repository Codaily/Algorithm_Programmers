from collections import deque
def solution(begin, target, words):
    answer = 0 
    visited = [False for i in range(len(words))]
    q = deque()
    q.append(begin)
    while q:
        answer += 1
        prev = q.popleft()
        for i in range(len(words)):
            if visited[i] == False and compare(prev, words[i]):
                if words[i] == target:
                    return answer
                
                visited[i] = True
                q.append(words[i])
    if prev != target:
        return 0           
    return answer

def compare(w1, w2):
    count = 0
    for i1, i2 in zip(w1, w2):
        if i1 != i2:
            count += 1
        if count > 1:
            return False
    return True
