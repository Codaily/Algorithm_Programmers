from collections import deque
def solution(numbers, target):
    answer = 0
    que = deque([(0, 0)])
    while que:
        s, l = que.popleft()
        if l > len(numbers):
            break
        elif s == target and l == len(numbers):
            answer += 1
        que.append((s+numbers[l-1] , l+1))
        que.append((s-numbers[l-1], l+1))
    return answer
        
print(solution([4, 1, 2, 1],3))

# python이라면 이정도...
# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)

